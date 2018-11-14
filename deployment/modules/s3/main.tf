resource "aws_s3_bucket" "anchor-aid" {
  bucket = "anchor-aid"
}

resource "local_file" "s3-bucket-config" {
    content     = "S3_BUCKET = '${aws_s3_bucket.anchor-aid.id}'"
    filename = "../../s3_bucket_config.py"
}