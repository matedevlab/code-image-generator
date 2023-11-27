import unittest
from flask import template_rendered
from contextlib import contextmanager
from app import app


class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.context = app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    @contextmanager
    def captured_templates(self):
        recorded = []

        def record(sender, template, context, **extra):
            recorded.append((template, context))

        template_rendered.connect(record, app)
        try:
            yield recorded
        finally:
            template_rendered.disconnect(record, app)

    def test_root_route(self):
        with self.captured_templates() as templates:
            response = self.app.get("/")
            self.assertEqual(response.status_code, 200)

            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, "code_input.html")
            self.assertIn("num_lines", context)
            self.assertIn("max_chars", context)


if __name__ == "__main__":
    unittest.main()
