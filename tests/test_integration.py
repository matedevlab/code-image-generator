import unittest
from app import app


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.context = app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_code_and_style_integration(self):
        # Submit code
        self.app.post("/save_code", data={"code": 'print("Hello World")'})
        # Check if the code is saved in session
        with self.app.session_transaction() as session:
            self.assertEqual(session["code"], 'print("Hello World")')

        # Submit style
        self.app.post("/save_style", data={"style": "monokai"})
        # Check if the style is saved in session
        with self.app.session_transaction() as session:
            self.assertEqual(session["style"], "monokai")


if __name__ == "__main__":
    unittest.main()
