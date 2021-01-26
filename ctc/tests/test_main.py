"""Contains tests for main"""
from unittest import TestCase

from app.main import app
from webtest_asgi import TestApp


class TestMain(TestCase):
    """Contains tests for Main"""

    app: TestApp

    def setUp(self):
        """Sets up test env"""
        self.app = TestApp(app)

    def test_main_response(self):
        """Tests the response from main"""
        resp = self.app.get("/")
        self.assertEqual(resp.status_int, 200)

    def test_main_content(self):
        """Tests the response content from main"""
        resp = self.app.get("/")
        self.assertEqual(resp.content_type, "application/json")
        self.assertIn("message", resp.json.keys())
