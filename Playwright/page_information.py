from http import cookies
from idlelib import browser

import time

import pytest
from playwright.sync_api import sync_playwright

SUPPORTED_BROWSERS = ["firefox", "chromium", "edge", "safari", "webkit"]

BROWSER_NAME = "chromium"

URL = "https://www.google.com"

HEADED_MODE = False

@pytest.fixture(scope="class")
def setup(request):
    print("PLAYWRIGHT PAGE INFORMATION" , "Browser Name : ", BROWSER_NAME)

    playwright = sync_playwright().start()

    match BROWSER_NAME:
        case "chromium":
            browser = playwright.chromium.launch(headless=HEADED_MODE)
        case "firefox":
            browser = playwright.firefox.launch(headless=HEADED_MODE)
        case "edge":
            browser = playwright.edge.launch(headless=HEADED_MODE)
        case "webkit":
            browser = playwright.webkit.launch(headless=HEADED_MODE)
        case _:
            raise ValueError(f"Browser {BROWSER_NAME} is not supported.")


    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width":1920, "height":1080})
    page.goto(URL)
    request.cls.page = page

    yield

    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestPageInformation():
    def testBrowserCurrentUrl(self):
        time.sleep(2)
        print("Page Tittle :",self.page.title() )
        current_url = self.page.url
        print("Current URL :",current_url)

    def testPageSource(self):
        time.sleep(2)
        page_content = self.page.content()
        print("Page Content / Source :",page_content)

    def testFetchCookie(self):
        time.sleep(2)
        page_cookies = self.page.context.cookies()
        print("Page Cookie :",page_cookies)

    def test_add_cookies(self):
        self.page.wait_for_timeout(2000) # 2 seconds
        cookie = {"name": "test", "value": "test_value"}
        self.page.context.add_cookies([cookie])

        cookies = self.page.context.cookies()
        cookies_name = [c["name"] for c in cookies]
        print(cookies_name)



