data "external" "zappa_project_name" {
  program = ["/bin/sh", "${path.module}/get-zappa-project-name.sh"]
}

resource "aws_iam_policy" "s3-bucket-policy" {
  name        = "anchor-aid-bucket-access"
  description = "Get and Put access to anchor-aid s3 bucket"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": ["${var.s3_bucket_arn}/*"]
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "s3_bucket_policy_attachment" {
  role       = "${data.external.zappa_project_name.result["name"]}-production-ZappaLambdaExecutionRole"
  policy_arn = "${aws_iam_policy.s3-bucket-policy.arn}"
}