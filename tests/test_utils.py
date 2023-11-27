import unittest
from unittest.mock import patch, MagicMock
from utils import take_screenshot_from_url


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_url = "http://localhost:5000/style"
        self.cookies = {"name": "test", "value": "test", "url": self.test_url}

    def test_take_screenshot_from_url(self):
        # Setup a mock for the screenshot function
        mock_screenshot_data = b"test_screenshot_data"
        with patch("utils.sync_playwright") as mock_sync_playwright:
            mock_browser = MagicMock()
            mock_page = MagicMock()
            mock_page.wait_for_selector.return_value.screenshot.return_value = (
                mock_screenshot_data
            )
            mock_context = MagicMock(new_page=MagicMock(return_value=mock_page))
            mock_browser.chromium.launch.return_value.new_context.return_value = (
                mock_context
            )
            mock_sync_playwright.return_value.__enter__.return_value = mock_browser

            # Call the function and assert its behavior
            result = take_screenshot_from_url(self.test_url, self.cookies)
            self.assertEqual(result, mock_screenshot_data)

            # Assertions to ensure the correct flow within the mocked Playwright
            mock_browser.chromium.launch.assert_called_once()
            mock_context.new_page.assert_called_once()
            mock_page.goto.assert_called_with(self.test_url)
            mock_page.wait_for_selector.assert_called_once()


if __name__ == "__main__":
    unittest.main()
