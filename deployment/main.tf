provider "aws" {
  region  = "${var.region}"
  profile = "scottx611x@gmail.com"
}

module "s3" {
  source  = "./modules/s3"
}

module "iam" {
  source  = "./modules/iam"
  s3_bucket_arn = "${module.s3.s3_bucket_arn}"
}