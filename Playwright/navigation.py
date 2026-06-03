import time

import playwright
import pytest
from playwright.sync_api import sync_playwright

SUPPORTED_BROWSER_NAMES = ["chromium", "firefox", "edge", "safari", "webkit"]

BROWSER_NAME = "chromium"

HEADED_MODE = False

URL = "https://www.google.com"

@pytest.fixture(scope="class")
def setup(request):
    print("Browser name :", BROWSER_NAME)
    playwright = sync_playwright().start()

    match BROWSER_NAME:
        case "chromium":
            browser = playwright.chromium.launch(headless=HEADED_MODE)
        case"firefox":
            browser = playwright.firefox.launch(headless=HEADED_MODE)
        case "edge":
            browser = playwright.edge.launch(headless=HEADED_MODE)
        case "safari":
            browser = playwright.safari.launch(headless=HEADED_MODE)
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
class TestNavigation:
    def test_navigation(self):
        self.page.wait_for_timeout(2000)
        tittle = self.page.title()
        print("Page Tittle is : ", tittle)
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        tittle = self.page.title()
        print("Page Tittle is : ", tittle)
        time.sleep(2)
        #back
        self.page.go_back()
        tittle = self.page.title()
        print("Page Tittle is : ", tittle)
        time.sleep(2)

        # Forward - 2nd URL
        self.page.go_forward()
        time.sleep(2)
        tittle = self.page.title()
        print("Page Tittle is : ", tittle)
        time.sleep(2)

        #reload
        self.page.reload()
        time.sleep(2)
        tittle = self.page.title()
        print("Page Tittle is : ", tittle)
        time.sleep(2)




