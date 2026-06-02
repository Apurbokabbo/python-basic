import time

import pytest
from playwright.sync_api import sync_playwright, expect

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/hovers.html"

#Step 4: Setup + Teardown

@pytest.fixture(scope="class")
def setup(request):
    print(f"Starting {BROWSER_NAME} browser....")

    # Step 5: Start Playwright
    playwright = sync_playwright().start()
    playwright.selectors.set_test_id_attribute("data-test-id")

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
class TestMouseHover:

    @pytest.fixture(autouse=True)
    def reset_mouse_position(self):
        yield
        if hasattr(self, "page"):
            self.page.mouse.move(0,0)
            self.page.wait_for_timeout(300)

    def test_mouse_hover_example1(self):
        services = self.page.get_by_test_id("nav-services")
        expect(services).to_be_visible()
        services.hover()
        time.sleep(2)

        consulting = self.page.get_by_test_id("nav-consulting")
        consulting.hover()
        time.sleep(2)

    def test_mouse_hover_example2(self):
        menu = self.page.get_by_test_id("tree-menu-root")
        expect(menu).to_be_visible()
        menu.hover()
        time.sleep(2)

        electronics = self.page.get_by_test_id("tree-l2-electronics")
        electronics.hover()
        time.sleep(2)

        audio = self.page.get_by_test_id("tree-l3-audio")
        audio.hover()
        time.sleep(2)

    def test_mouse_hover_example3(self):
        security = self.page.get_by_test_id("security-reveal")
        expect(security).to_be_visible()
        security.hover()
        time.sleep(2)
        expect(security).to_contain_text("SECRET_API_TOKEN_99")
        time.sleep(2)

    def test_mouse_hover_example4(self):
        progress = self.page.get_by_test_id("progress-trigger")
        percent = self.page.locator("#progress-percent")
        expect(progress).to_be_visible()
        progress.hover()
        time.sleep(2)
        expect(percent).to_have_text("100%", timeout=5000)
        time.sleep(2)

