import unittest
from app import app


class TestFormsAndSessions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.context = app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_save_code(self):
        response = self.app.post("/save_code", data={"code": 'print("Hello")'})
        with self.app.session_transaction() as session:
            self.assertEqual(session["code"], 'print("Hello")')
        self.assertEqual(response.status_code, 302)  # Assuming redirection occurs

    def test_save_style(self):
        response = self.app.post(
            "/save_style", data={"style": "monokai", "code": 'print("Hello")'}
        )
        with self.app.session_transaction() as session:
            self.assertEqual(session["style"], "monokai")
            self.assertEqual(session["code"], 'print("Hello")')
        self.assertEqual(response.status_code, 302)  # Assuming redirection occurs


if __name__ == "__main__":
    unittest.main()
