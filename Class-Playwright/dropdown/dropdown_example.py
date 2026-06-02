import time

import pytest
from playwright.sync_api import sync_playwright

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/dropdown.html"

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
class TestDropdown:
    """Locating by ID"""
    def test_dropdown_example_1(self):
        dropdown = self.page.locator("#amazon-sort")
        dropdown.select_option("rating")
        time.sleep(5)

    def test_dropdown_example_2(self):
        dropdown = self.page.locator("#color-dropdown")
        dropdown.select_option("red")
        time.sleep(5)

    def test_dropdown_example_3(self):
        dropdown = self.page.locator("#skills-multi")
        dropdown.select_option(["js","py","pw"])
        time.sleep(5)

    def test_dropdown_by_index(self):
        dropdown = self.page.locator("#amazon-sort")
        dropdown.select_option(index=2)
        time.sleep(5)

    def test_dropdown_example_4(self):
        dropdown = self.page.locator("#country-select")
        dropdown.select_option(index=2)
        time.sleep(5)

        city = self.page.locator("#city-select")
        city.select_option(index=2)
        time.sleep(5)

        neigh = self.page.locator("#neigh-select")
        neigh.select_option(index=1)
        time.sleep(5)

    def test_dropdown_search(self):
        self.page.locator("#repo-search").fill("facebook")
        time.sleep(5)
        dropdown = self.page.locator("#repo-list")
        dropdown.select_option("react")
        print(f"Text: {dropdown.text_content()}")

        time.sleep(5)
# Note:
    def test_dropdown_search2(self):
        self.page.locator("#repo-search").fill("a")
        time.sleep(5)

        options = self.page.locator("#repo-list option")
        count = options.count()
        print(f"Count: {count}")
        for i in range(count):
            option = options.nth(i)
            style = option.get_attribute("style")
            print(f"Style: {style}")
            if style and "display: block" in style:
                print(option.text_content())