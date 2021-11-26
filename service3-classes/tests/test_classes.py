import unittest
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestClasses(TestBase):
    def test_classes(self):
        response = self.client.get(url_for('classes'))
        self.assertEqual(response.status_code, 200)