import json
from urllib.parse import urlparse

from flask_app.s3_bucket_config import S3_BUCKET

import boto3

session = boto3.Session(profile_name='scottx611x@gmail.com')
s3 = session.resource("s3").Bucket(S3_BUCKET)


def is_valid_url(url):
    parse_result = urlparse(url)
    return parse_result.scheme and parse_result.netloc


def validate_form_data(post_data):
    site = post_data.get("site")
    search = post_data.get("search")
    return is_valid_url(site) and isinstance(search, str)


def load_s3(key):
    return json.load(s3.Object(key=key).get()["Body"])


def dump_s3(key, obj):
    s3.Object(key=key).put(Body=json.dumps(obj))
