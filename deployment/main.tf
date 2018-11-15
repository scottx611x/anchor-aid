provider "aws" {
  region  = "${var.region}"
  version = "1.41.0"
}

provider "external" {
  version = "~> 1.0"
}

provider "local" {
  version = "~> 1.1"
}


module "s3" {
  source  = "./modules/s3"
  s3_bucket_name = "${var.s3_bucket_name}"
}

module "iam" {
  source  = "./modules/iam"
  s3_bucket_arn = "${module.s3.s3_bucket_arn}"
}