import time
import pytest
from playwright.sync_api import sync_playwright, expect

# Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

# Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/hovers.html"
ALERT_URL = "https://automation.ebrahimhossain.com.bd/alerts.html"


# Step 4: Setup + Teardown

@pytest.fixture(scope="class")
def setup(request):
    print(f"Starting {BROWSER_NAME} browser....")

    # Step 5: Start Playwright
    playwright = sync_playwright().start()
    # playwright.selectors.set_test_id_attribute("data-test-id")

    # Step 6: Launch the browser
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

    # Step 8: Create a new page
    page = context.new_page()
    # Viewport - Screen Size
    page.set_viewport_size({"width": 1920, "height": 1080})

    # Step 9: Open the URL
    page.goto(ALERT_URL)
    time.sleep(5)

    request.cls.page = page

    # YIELD = Tests Run Here.....
    yield

    # Teardown
    context.close()
    browser.close()
    playwright.stop()


@pytest.mark.usefixtures("setup")
class TestAlerts:
    def test_native_alert(self):
        self.page.wait_for_load_state("load")

        def handle_alert(dialog):
            print("Type: ", dialog.type)
            print("Message: ", dialog.message)
            dialog.accept()
            time.sleep(2)

        self.page.once("dialog", handle_alert)
        self.page.locator("#alertBtn").click()
        time.sleep(2)

    def test_confirm_alert(self):
        self.page.wait_for_load_state("load")

        def handle_alert(dialog):
            print("Type: ", dialog.type)
            print("Message: ", dialog.message)
            dialog.dismiss()
            time.sleep(2)

        self.page.once("dialog", handle_alert)
        self.page.locator("#confirmBtn").click()
        time.sleep(2)

    def test_prompt_alert(self):
        self.page.wait_for_load_state("load")

        def handle_alert(dialog):
            print("Type: ", dialog.type)
            print("Message: ", dialog.message)
            dialog.accept()
            time.sleep(2)

        self.page.once("dialog", handle_alert)
        self.page.locator("#promptBtn").click()
        time.sleep(2)

    def test_toast_success(self):
        self.page.wait_for_load_state("load")
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator("[data-testid='toast-success-btn']").click()
        time.sleep(2)

        toast_success = self.page.locator("[data-testid='toast-success-item']")
        expect(toast_success).to_contain_text("Success! Record updated.")

    def test_toast_hide(self):
        self.page.wait_for_load_state("load")
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator("[data-testid='toast-info-btn']").click()
        time.sleep(2)

        toast_success = self.page.locator("[data-testid='toast-info-item']")
        expect(toast_success).to_contain_text("System will restart in 5 minutes.")

        expect(toast_success).not_to_be_visible(timeout=7000)

