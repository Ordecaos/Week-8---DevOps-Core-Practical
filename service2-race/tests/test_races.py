import unittest
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRace(TestBase):
    def test_race(self):
        response = self.client.get(url_for('races'))
        self.assertEqual(response.status_code, 200)