provider "aws" {
  region  = "${var.region}"
}

resource "aws_s3_bucket" "anchor-aid" {
  bucket = "anchor-aid"
}

resource "local_file" "s3-bucket-config" {
    content     = "S3_BUCKET = '${aws_s3_bucket.anchor-aid.id}'"
    filename = "../flask_app/s3_bucket_config.py"
}