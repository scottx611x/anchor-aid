import json
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


def is_valid_url(url):
    result = urlparse(url)
    return all([result.scheme, result.netloc])


def validate_form_data(post_data):
    site = post_data.get("site", "")
    search = post_data.get("search")
    if not any([
        site.startswith(scheme) for scheme in ["http://", "https://"]
    ]):
        site = "http://" + site
    if is_valid_url(site) and isinstance(search, str):
        return {"site": site, "search": search}


class S3Interface:
    def __init__(self, app):
        self.s3_client = app.config.get("S3_CLIENT")

    def load(self, key):
        return json.load(self.s3_client.Object(key=key).get()["Body"])

    def dump(self, key, obj):
        self.s3_client.Object(key=key).put(Body=json.dumps(obj))
