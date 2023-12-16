from playwright.sync_api import sync_playwright
from gevent import monkey

monkey.patch_all()


def take_screenshot_from_url(url, session_data):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context(device_scale_factor=2)
        page = context.new_page()
        context.add_cookies([session_data])
        page.goto(url, timeout=30000)
        code_element = page.wait_for_selector(".code", timeout=30000)
        screenshot_bytes = code_element.screenshot()
        page.close()
        context.close()
        browser.close()
        return screenshot_bytes
