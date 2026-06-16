import time
import pytest
from playwright.sync_api import sync_playwright, expect

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]
# Step 2: Define the browser
BROWSER_NAME = "chromium"
#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/form.html"

#Step 4: Setup + Teardown
@pytest.fixture(scope="class")
def setup(request):
    print(f"Starting {BROWSER_NAME} browser....")
    # Step 5: Start Playwright
    playwright = sync_playwright().start()
    #Step 6: Launch the browser
    if BROWSER_NAME == "chromium":
        browser = playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
    elif BROWSER_NAME == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif BROWSER_NAME == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Browser {BROWSER_NAME} is not supported.")
    # Step 7: create browser context
    context = browser.new_context()
    #Step 8: Create a new page
    page = context.new_page()
    # Viewport - Screen Size
    page.set_viewport_size({"width": 1920, "height": 1080})
    #Step 9: Open the URL
    page.goto(URL)
    request.cls.page = page

    # YIELD = Tests Run Here.....
    yield
    # Teardown
    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestWaits:
    def test_wait_for_timeout(self):
        self.page.wait_for_timeout(3000)

    def test_wait_for_locator(self):
        firstName = self.page.locator("#firstName")
        firstName.wait_for(state='visible')
        firstName.fill("Ebrahim")

    def test_wait_for_selector(self):
        self.page.wait_for_selector("#maritalStatus")

    def test_wait_for_full_page_load(self):
        self.page.goto("https://www.daraz.com.bd/")
        self.page.wait_for_load_state("load")

    def test_wait_for_url(self):
        self.page.goto("https://www.daraz.com.bd/")
        self.page.wait_for_url("**daraz.com**")

    def test_wait_for_attribute(self):
        first_name = self.page.locator("#firstName")
        expect(first_name).to_have_attribute(
            "placeholder", "First Name"
        )

    def test_wait_for_response(self):
        with self.page.expect_response(lambda r: r.status == 200):
            self.page.reload()