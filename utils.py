from playwright.sync_api import sync_playwright


def take_screenshot_from_url(url, session_data):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        browser_context = browser.new_context(device_scale_factor=2)
        browser_context.add_cookies([session_data])
        page = browser_context.new_page()
        page.goto(url)
        page.wait_for_selector(".code")
        screenshot_bytes = page.screenshot()
        browser.close()
        return screenshot_bytes
