import time
from multiprocessing import context
from unittest import case

import playwright
import pytest
from playwright.sync_api import sync_playwright
from virtualenv.util import error

from Basic.Conditions.shorthand import browser

BROWSER_SUPPORTED = ["chromium","edge","firefox","safari","webkit"]
BROWSER_NAME = "chromium"
HEADED_MODE = False
URL = "https://automation.ebrahimhossain.com.bd/form.html"

@pytest.fixture(scope="class")
def setup(request):
    print("Browser: ",BROWSER_SUPPORTED)
    print("Headed: ",HEADED_MODE)
    print("Browser Name: ",BROWSER_NAME)

    playwright = sync_playwright().start()

    match BROWSER_NAME:
        case "edge":
            browser = playwright.edge.launch(
                headless=HEADED_MODE,
                args=["--disable-blink-features=AutomationControlled"],
            )
        case "firefox":
            browser = playwright.firefox.launch(
                headless=HEADED_MODE,
                args=["--disable-blink-features=AutomationControlled"],
            )
        case "chromium":
            browser = playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            )

        case "safari":
            browser = playwright.safari.launch(
                headless=HEADED_MODE,
                args=["--disable-blink-features=AutomationControlled"],
            )
        case "webkit":
            browser = playwright.webkit.launch(
                headless=HEADED_MODE,
                args=["--disable-blink-features=AutomationControlled"],
            )
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
class TestLocatorFinder:
    """Locating by ID"""
    def test_by_id(self):
        first_name = self.page.locator("#firstName")  # For Class -> Dot(.), For Id -> #
        first_name.fill("Apurbo")
        last_name = self.page.locator("#lastName")
        last_name.fill("Kabbo")
        time.sleep(2)

    """Locating by Name"""
    def test_by_name(self):
        nid = self.page.locator("[name='national_id']")
        nid.fill("75012121212")
        time.sleep(2)


    """Locating by Class Name"""
    def test_by_class_name(self):
        email_field = self.page.locator(".form-input").nth(6)
        email_field.fill("apurbokabbo1999@gmail.com")
        time.sleep(5)

    def test_by_class2(self):
        dropdown = self.page.locator(".form-select").nth(0)
        dropdown.click()
        time.sleep(2)

    """Locating by Tag"""
    def test_by_tag_name(self):
        sections = self.page.locator("section")
        print("Plain : ",sections)
        print(f"Total Sections: {sections.count()}")
        time.sleep(2)

    """Locating by Link"""
    def test_by_link(self):
        back_to_home = self.page.locator("a:has-text('Back to Home')")
        back_to_home.click()
        time.sleep(2)

    """Locating by CSS Selector"""
    def test_by_css_selector(self):
        # tagName[attributeName='value']
        last_name = self.page.locator("input[placeholder='Full name']")
        last_name.fill("Hossain")
        time.sleep(2)

    """Locating by xpath"""
    def test_by_xpath(self):
        """
        Xpath Syntax: //tagName[@attribute_name='attribute_value']
        """
        email = self.page.locator("//input[@placeholder='e.g. IT']")

        email.fill("IT")
        time.sleep(3)




