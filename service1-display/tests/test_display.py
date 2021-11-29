import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app, db, Characters

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                DEBUG=True,
                )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Characters(dbrace="Human", dbclass="Fighter", dbname="Om", dbtitle="Brave")
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_view_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_gen(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2-race:5000/char/races', text='Human')
            m.get('http://service3-classes:5000/char/classes', text='Fighter')
            m.post('http://service4-name:5000/char/name', text='Om')
            m.post('http://service4-name:5000/char/title', text='Brave')
            response = self.client.get(url_for('generator'))
            self.assertEqual(response.status_code, 200)
    
    def test_check_gen(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2-race:5000/char/races', text='Human')
            m.get('http://service3-classes:5000/char/classes', text='Fighter')
            m.post('http://service4-name:5000/char/name', text='Om')
            m.post('http://service4-name:5000/char/title', text='Brave')
            response = self.client.get(url_for('generator'))
            self.assertIn(b'You are a Human you trained as a Fighter and your name is Om the Brave.', response.data)

    def test_last_five(self):
        response = self.client.get(url_for('generator'))
        self.assertIn(b'You are a Human you trained as a Fighter and your name is Om the Brave.', response.data)