import time
import pytest
from playwright.sync_api import sync_playwright, expect

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]
# Step 2: Define the browser
BROWSER_NAME = "chromium"
#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/form.html"
BUTTON_URL = "https://automation.ebrahimhossain.com.bd/buttons.html"

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
    # page.goto(URL)
    request.cls.page = page

    # YIELD = Tests Run Here.....
    yield
    # Teardown
    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestStates:
    """Locating by ID"""
    def test_is_enabled(self):
        self.page.goto(BUTTON_URL)
        button = self.page.locator("#btn-standard")
        print("Enabled: ", button.is_enabled())
        time.sleep(3)

    def test_is_disabled(self):
        self.page.goto(BUTTON_URL)
        button = self.page.locator("#btn-disabled")
        print("Enabled: ", button.is_disabled())
        time.sleep(3)

    def test_is_editable(self):
        self.page.goto(URL)
        firstName = self.page.locator("#firstName")
        print("Editable: ", firstName.is_editable())
        time.sleep(3)

    def test_is_checked(self):
        self.page.goto(URL)
        checkbox = self.page.locator("input[type=checkbox]").first
        checkbox.check()
        time.sleep(2)
        print("Checked: ", checkbox.is_checked())
        time.sleep(3)

    def test_expected_visible(self):
        self.page.goto(URL)
        locator = self.page.locator("#firstName")
        res = expect(locator).to_be_visible()
        print("Locator is visible", res)
        time.sleep(3)

    def test_is_editable(self):
        self.page.goto(URL)
        firstName = self.page.locator("#firstName")
        firstName.fill("GTA")
        expect(firstName).to_have_value("GTA")
        time.sleep(3)