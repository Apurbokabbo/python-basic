import time
import pytest
from playwright.sync_api import sync_playwright

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]
# Step 2: Define the browser
BROWSER_NAME = "chromium"
#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/iframes.html"

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
class TestIframes:
    """Locating by ID"""
    def test_iframe(self):
        time.sleep(2)

        payment_frame = self.page.frame_locator("#payment-frame")
        card_holder_name = payment_frame.locator("#card-holder")
        card_holder_name.fill("Ebrahim Hossain")

        card_number = payment_frame.locator("#card-number")
        card_number.fill("4111 1111 1111 1111")
        time.sleep(5)

        editor_frame = self.page.frame_locator("#editor-frame")
        editor_body = editor_frame.locator("#editor-body")
        editor_body.fill("This is a frame")
        time.sleep(5)

        # Nested ->
        # firstFrame = self.page.frame_locator()
        # secondFrame = firstFrame.frame_locator()
        # thirdFrame = secondFrame.frame_locator()
        # ......