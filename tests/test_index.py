# coding=utf-8
import uuid
from contextlib import contextmanager
from unittest import TestCase

from flask import template_rendered

from index import app
from s3_bucket_config import S3_BUCKET

import boto3
from moto import mock_s3

from utils import dump_s3


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


class GenericTestBase(TestCase):
    def setUp(self):
        self.app = app
        self.test_client = self.app.test_client()


@mock_s3
class RoutesTestCase(GenericTestBase):
    def setUp(self):
        super().setUp()
        self.s3_client = boto3.client("s3")
        self.s3_client.create_bucket(Bucket=S3_BUCKET)

    def test_index_route(self):
        with captured_templates(self.app) as templates:
            response = self.test_client.get('/')
        self.assertEquals(response.status_code, 200)
        template, context = templates[0]
        self.assertEqual(template.name, 'base.html')
        self.assertIsNone(context.get("search"))
        self.assertIsNone(context.get("site"))

    def test_index_route_with_uuid(self):
        key = str(uuid.uuid4())
        data = {"search": "test", "site": "http://www.example.com"}
        dump_s3(key, data)

        with captured_templates(self.app) as templates:
            response = self.test_client.get('/' + key)
        self.assertEquals(response.status_code, 200)
        template, context = templates[0]
        self.assertEqual(template.name, 'anchor-aid.html')
        self.assertIsNotNone(context.get("search"))
        self.assertIsNotNone(context.get("site"))

    def test_index_route_with_bad_uuid(self):
        key = str(uuid.uuid4())
        response = self.test_client.get('/' + key)
        self.assertEquals(response.status_code, 400)

    def test_create_redirects_to_new_page(self):
        data = {"search": "test", "site": "http://www.example.com"}
        response = self.test_client.post('/create', data=data)
        self.assertEquals(response.status_code, 302)

    def test_create_route_bad_url(self):
        data = {"search": "test", "site": ""}
        response = self.test_client.post('/create', data=data)
        self.assertEquals(response.status_code, 400)
        self.assertEqual(response.data, b"Bad Request")

    def test_create_route_without_url_scheme_still_works(self):
        data = {"search": "test", "site": "www.example.com"}
        response = self.test_client.post('/create', data=data)
        self.assertEquals(response.status_code, 302)

