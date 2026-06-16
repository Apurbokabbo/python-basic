from idlelib import browser
from multiprocessing import context
from unittest import case

import pytest
import time
from openpyxl.worksheet import page
from playwright.sync_api import sync_playwright, expect

SUPPORTED_BROWSERS = ["firefox", "chromium","edge"]

BROWSER_NAME = "chromium"

HEADED_MODE = False

URL = "https://automation.ebrahimhossain.com.bd/hovers.html"

@pytest.fixture(scope="class")
def setup(request):

    playwright = sync_playwright().start()
    playwright.selectors.set_test_id_attribute("data-test-id")
    playwright.selectors.set_test_id_attribute("get_by_role")

    match BROWSER_NAME:

        case "chromium":
            browser = playwright.chromium.launch(
                headless=HEADED_MODE,
                args=["--disable-blink-features=AutomationControlled"],
            )

        case "edge":
            browser = playwright.edge.launch(
                headless=HEADED_MODE,
            )

        case "firefox":
            browser = playwright.firefox.launch(
                headless=HEADED_MODE,
                args=["--disable-blink-features=AutomationControlled"],
            )

        case _:
            raise ValueError(f"Browser {BROWSER_NAME} is not supported.")

    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(URL)
    request.cls.page = page

    yield

    context.close()
    browser.close()
    playwright.stop()


@pytest.mark.usefixtures("setup")
class TestMouseHover():
    def test_mouse_hover_example(self):
        service = self.page.locator("//button[normalize-space(text())='Services']")
        expect(service).to_be_visible()
        service.hover()
        time.sleep(2)
        consulting = self.page.locator("//button[normalize-space(text())='Consulting']")
        consulting.hover()
        time.sleep(2)
        self.page.get_by_role("link", name="QA Automation Audit").click()
        time.sleep(2)

    def test_mouse_hover_example2(self):
        category = self.page.get_by_role("button", name="Explore Categories")
        expect(category).to_be_visible()
        category.hover()
        time.sleep(2)
        electronics = self.page.get_by_role("button", name="Electronics")
        electronics.hover()
        time.sleep(2)
        audio = self.page.get_by_role("button", name="Audio")
        audio.hover()
        time.sleep(2)
        self.page.get_by_role("link", name="Wireless Earbuds").click()
        time.sleep(2)





