import time
import pytest
from playwright.sync_api import sync_playwright

BROWSER_NAME = "chromium"
HEADED_MODE = False
URL = "https://automation.ebrahimhossain.com.bd/dropdown.html"


@pytest.fixture(scope="class")
def setup(request):
    playwright = sync_playwright().start()

    browser = None
    context = None

    try:
        match BROWSER_NAME:
            case "chromium":
                browser = playwright.chromium.launch(headless=False)
            case "firefox":
                browser = playwright.firefox.launch(headless=HEADED_MODE)
            case _:
                raise ValueError("Unsupported browser")

        context = browser.new_context()
        page = context.new_page()
        page.goto(URL)

        # ✅ ATTACH EVERYTHING (VERY IMPORTANT)
        request.cls.playwright = playwright
        request.cls.browser = browser
        request.cls.context = context
        request.cls.page = page

        yield

    finally:
        if context:
            context.close()
        if browser:
            browser.close()
        playwright.stop()

@pytest.mark.usefixtures("setup")
class TestDropDown:
    def test_dropdown_example_1(self):
        dropdown = self.page.locator("#amazon-sort")
        dropdown.select_option("Newest Arrivals")
        time.sleep(2)

    def test_dropdown_example_2(self):
        dropdown = self.page.locator("#color-dropdown")
        dropdown.select_option("red") #value
        time.sleep(2)

    def test_dropdown_example_3(self):
        dropdown = self.page.locator("#skills-multi")
        dropdown.select_option(["py","js","sql"]) #value with multiple
        time.sleep(2)

    def test_dropdown_example_4(self):
        dropdown = self.page.locator("#amazon-sort")
        dropdown.select_option(index=3) #index
        time.sleep(2)