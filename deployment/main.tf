provider "aws" {
  region  = "${var.region}"
}

module "s3" {
  source  = "./modules/s3"
  s3_bucket_name = "${var.s3_bucket_name}"
}

module "iam" {
  source  = "./modules/iam"
  s3_bucket_arn = "${module.s3.s3_bucket_arn}"
}