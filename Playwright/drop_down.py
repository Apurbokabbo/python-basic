import time
import pytest
from playwright.sync_api import sync_playwright

BROWSER_NAME = "chromium"
HEADED_MODE = False
URL = "https://automation.ebrahimhossain.com.bd/dropdown.html"


@pytest.fixture(scope="class")
def setup(request):
    print(f"Starting {BROWSER_NAME} browser....")

    playwright = sync_playwright().start()

    try:
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
            raise ValueError("Unsupported browser")

        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})

        # ✅ FIX IS HERE
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)

        request.cls.playwright = playwright
        request.cls.browser = browser
        request.cls.context = context
        request.cls.page = page

        yield

    finally:
        context.close()
        browser.close()
        playwright.stop()

@pytest.mark.usefixtures("setup")
class TestDropDown:
    def test_dropdown_example_1(self):
        dropdown = self.page.locator("#amazon-sort")
        dropdown.select_option("Newest Arrivals")
        time.sleep(2)

    def test_dropdown_example_2(self):
        dropdown = self.page.locator("#color-dropdown")
        dropdown.select_option("red") #value
        time.sleep(2)

    def test_dropdown_example_3(self):
        dropdown = self.page.locator("#skills-multi")
        dropdown.select_option(["py","js","sql"]) #value with multiple
        time.sleep(2)

    def test_dropdown_example_4(self):
        dropdown = self.page.locator("#amazon-sort")
        dropdown.select_option(index=3) #index
        time.sleep(2)

    def test_dropdown_example_5(self):
        country = self.page.locator("#country-select")
        country.select_option(index=2) #index
        time.sleep(1)

        city = self.page.locator("#city-select")
        city.select_option(index=2)
        time.sleep(1)

        neigh = self.page.locator("#neigh-select")
        neigh.select_option(index=1)
        time.sleep(2)

    def test_dropdown_example_6(self):
        search_field = self.page.locator("#repo-search") #search and select
        search_field.fill("angular")
        time.sleep(2)
        dropdown = self.page.locator("#repo-list")
        dropdown.select_option("angular")
        print(f"Text: {dropdown.text_content()}")
        time.sleep(2)


    def test_dropdown_search2(self):
        self.page.locator("#repo-search").fill("angular")
        time.sleep(3)

        options = self.page.locator("#repo-list option")

        count = options.count()
        print(f"Count: {count}")


        for i in range(count):
            option = options.nth(i)
            style = option.get_attribute("style")
            print(f"Style: {style}")
            if style and "display: block" in style:
                print(option.text_content())









