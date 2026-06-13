import time
import pytest
from playwright.sync_api import sync_playwright

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
class TestUniversal:

    def test_by_id(self):
        self.page.get_by_label("First Name").fill("GTA")

