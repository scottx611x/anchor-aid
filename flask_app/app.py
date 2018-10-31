import json

import boto3
from flask import Flask
from flask import render_template

from s3_bucket_config import S3_BUCKET


SITE = "http://github.com/refinery-platform/refinery-platform/wiki/setting-up-newer-galaxy"
SEARCH = "You have to add a Galaxy Instance for the Galaxy installation in question to Refinery through the admin UI."

app = Flask(__name__)
app.debug = True

s3 = boto3.client("s3")


@app.route('/', methods=['GET'])
def index():
    return render_template("home.html", **{"site": SITE, "search": SEARCH})


@app.route('/list', methods=['GET'])
def list():
    return json.dumps(s3.list_objects(Bucket=S3_BUCKET))


@app.route('/create', methods=['GET'])
def create():
    return json.dumps(s3.list_objects(Bucket=S3_BUCKET))
