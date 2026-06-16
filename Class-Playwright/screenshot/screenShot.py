import time
import pytest
from playwright.sync_api import sync_playwright

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
class TestScreenShots:
    """Locating by ID"""
    def test_full_page_screenshots(self):
        time.sleep(2)
        self.page.screenshot(path="screenshots/full_page_screenshots.png", full_page=True)


    def test_default_page_screenshots(self):
        time.sleep(2)
        self.page.screenshot(path="screenshots/default_page_screenshots.png", full_page=False)

    def test_element_screenshots(self):
        time.sleep(2)
        element = self.page.locator("#firstName")
        element.screenshot(path="screenshots/firstName_screenshots.png")

    def test_specific_section_screenshots(self):
        time.sleep(2)
        element = self.page.locator("(//section[contains(@class,'practice-card p-6')])[1]")
        element.screenshot(path="screenshots/specific_section_screenshots.png")

    def test_specific_section2_screenshots(self):
        time.sleep(2)
        element = self.page.locator("(//section[contains(@class,'practice-card p-6')])[1]")
        element.screenshot(path="screenshots/specific_section_2_screenshots.jpg", quality=80)

    def test_transparent_screenshots(self):
        time.sleep(2)
        element = self.page.locator("(//section[contains(@class,'practice-card p-6')])[1]")
        element.screenshot(path="screenshots/transparent_screenshots.png", omit_background=True)

    def test_mobile_view_screenshots(self):
        time.sleep(2)
        self.page.set_viewport_size({"width": 375, "height": 812})
        time.sleep(2)
        self.page.screenshot(path="screenshots/mobile_view_screenshots.png", full_page=False)