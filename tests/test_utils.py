from unittest import TestCase

import boto3
from moto import mock_s3

from index import app, s3
from utils import is_valid_url, validate_form_data


class UtilitiesTestCase(TestCase):
    def test_is_valid_url_good_url(self):
        self.assertTrue(is_valid_url("http://www.example.com"))

    def test_is_valid_url_bad_url(self):
        self.assertFalse(is_valid_url("http:/www.example.com"))

    def test_validate_form_data_good_data(self):
        self.assertIsNotNone(
            validate_form_data(
                {
                    "site": "http://www.example.com",
                    "search": "hello"
                }
            )
        )

    def test_validate_form_data_bad_site(self):
        self.assertIsNotNone(
            validate_form_data(
                {
                    "site": "example.com",
                    "search": "hello"
                }
            )
        )

    def test_validate_form_data_bad_search(self):
        self.assertFalse(
            validate_form_data(
                {
                    "site": "http://www.example.com",
                    "search": {"hello": "world"}
                }
            )
        )

    def test_validate_form_data_no_site(self):
        self.assertFalse(validate_form_data({"search": "hello"}))

    def test_validate_form_data_no_search(self):
        self.assertFalse(
            validate_form_data({"site": "http://www.example.com"})
        )


@mock_s3
class AWSUtilitiesTestCase(TestCase):
    def setUp(self):
        self.s3_client = boto3.client("s3")
        self.s3_client.create_bucket(Bucket=app.config.get("S3_BUCKET"))

    def test_dump_and_load(self):
        s3.dump("dog", {"name": "Fido"})
        self.assertEqual(s3.load("dog")["name"], "Fido")
