"""Contains tests for greetings"""
from unittest import TestCase

from src.main import app
from webtest_asgi import TestApp
TestApp.__test__ = False


class TestGreetings(TestCase):
    """Contains tests for Greetings"""

    app: TestApp

    def setUp(self):
        """Sets up test env"""
        self.app = TestApp(app)

    def test_greetings_response(self):
        """Tests the response from greetings"""
        name = "John Doe"
        resp = self.app.get(f"/greet/{name}")
        self.assertEqual(resp.status_int, 200)

    def test_greetings_content(self):
        """Tests the response content from greetings"""
        resp = self.app.get("/")
        self.assertEqual(resp.content_type, "application/json")
        self.assertIn("message", resp.json.keys())
