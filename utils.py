import json
import logging
from urllib.parse import urlparse

from s3_bucket_config import S3_BUCKET

import boto3

s3 = boto3.resource("s3").Bucket(S3_BUCKET)

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


def load_s3(key):
    return json.load(s3.Object(key=key).get()["Body"])


def dump_s3(key, obj):
    s3.Object(key=key).put(Body=json.dumps(obj))
