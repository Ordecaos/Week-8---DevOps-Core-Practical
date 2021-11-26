import unittest
from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRaces(TestBase):
    def test_human(self):
        response = self.client.post(url_for("names"), data = "Human")
        if response == "Om":
            self.assertIn(b"Om", response.data)
        elif response == "Vardam":
            self.assertIn(b"Vardam", response.data)
        elif response == "Sondisk":
            self.assertIn(b"Sondisk", response.data)
    
    def test_elf(self):
        response = self.client.post(url_for("names"), data = "Elf")
        if response == "Beiran":
            self.assertIn(b"Beiran", response.data)
        elif response == "Pakian":
            self.assertIn(b"Pakian", response.data)
        elif response == "Zinyarus":
            self.assertIn(b"Zinyarus", response.data)
    
    def test_dragonborn(self):
        response = self.client.post(url_for("names"), data = "Dragonborn")
        if response == "Paravax":
            self.assertIn(b"Paravax", response.data)
        elif response == "Faccethir":
            self.assertIn(b"Faccethir", response.data)
        elif response == "Krochuas":
            self.assertIn(b"Krochuas", response.data)


class TestClasses(TestBase):
    def test_fighter(self):
        response = self.client.post(url_for("titles"), data = "Fighter")
        if response == "Brave":
            self.assertIn(b"Brave", response.data)
        elif response == "Strong":
            self.assertIn(b"Strong", response.data)
        elif response == "Tactical":
            self.assertIn(b"Tactical", response.data)

    def test_wizard(self):
        response = self.client.post(url_for("titles"), data = "Wizard")
        if response == "Wise":
            self.assertIn(b"Wise", response.data)
        elif response == "Powerful":
            self.assertIn(b"Powerful", response.data)
        elif response == "Devious":
            self.assertIn(b"Devious", response.data)
    
    def test_rogue(self):
        response = self.client.post(url_for("titles"), data = "Rogue")
        if response == "Cunning":
            self.assertIn(b"Cunning", response.data)
        elif response == "Cutthroat":
            self.assertIn(b"Cutthroat", response.data)
        elif response == "Silent":
            self.assertIn(b"Silent", response.data)
