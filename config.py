import os
import sys

import boto3
from botocore.exceptions import ProfileNotFound

from s3_bucket_config import S3_BUCKET


class Config(object):
    DEBUG = False
    TESTING = False
    AWS_PROFILE = None
    S3_BUCKET = S3_BUCKET
    S3_CLIENT = boto3.resource("s3").Bucket(S3_BUCKET)


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    AWS_PROFILE = "scottx611x@gmail.com"
    try:
        session = boto3.Session(profile_name=AWS_PROFILE)
    except ProfileNotFound:
        print(f"Profile: {AWS_PROFILE} was not found", sys.stderr)
    else:
        S3_CLIENT = session.resource("s3").Bucket(S3_BUCKET)


class TestingConfig(Config):
    TESTING = True


def set_app_config(app):
    if os.getenv("FLASK_TEST"):
        app.config.from_object('config.TestingConfig')
        return
    elif os.getenv("FLASK_DEV"):
        app.config.from_object('config.DevelopmentConfig')
        return
    else:
        app.config.from_object('config.ProductionConfig')
