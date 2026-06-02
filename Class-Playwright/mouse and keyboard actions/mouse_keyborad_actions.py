import time

import pytest
from playwright.sync_api import sync_playwright, expect

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/hovers.html"
BUTTON_URL = "https://automation.ebrahimhossain.com.bd/buttons.html"
FORM_URL = "https://automation.ebrahimhossain.com.bd/form.html"
DRAG_AND_DROP_URL = "https://automation.ebrahimhossain.com.bd/drag-and-drop.html"

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
class TestMouseAndKeyboardActions:
    def test_double_click(self):
        self.page.goto(BUTTON_URL)
        time.sleep(2)
        double_click = self.page.locator("#btn-dblclick").first
        double_click.dblclick()
        time.sleep(5)

    def test_right_click(self):
        self.page.goto(BUTTON_URL)
        time.sleep(2)
        right_click = self.page.locator("#btn-rightclick").first
        right_click.click(button="right")
        time.sleep(5)

    def test_click_and_hold(self):
        self.page.goto(BUTTON_URL)
        time.sleep(2)
        click_and_hold = self.page.locator("#btn-hold").first
        click_and_hold.hover()
        self.page.mouse.down()
        self.page.wait_for_timeout(3000)
        self.page.mouse.up()
        time.sleep(5)

    def test_move_to_element(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        element = self.page.locator("#github")
        element.scroll_into_view_if_needed()
        time.sleep(2)

    def test_scroll_down(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.evaluate("""
            window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        })
        """)
        time.sleep(2)

    def test_scroll_up(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.evaluate("""
            window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        })
        """)
        time.sleep(2)

        self.page.evaluate("""
                    window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                })
                """)
        time.sleep(2)

    def test_drag_and_drop(self):
        self.page.goto(DRAG_AND_DROP_URL)
        source = self.page.locator("#source-box")
        target = self.page.locator("#target-box")
        source.drag_to(target)
        time.sleep(2)
        target.drag_to(source)
        time.sleep(2)

    def test_keyboard_type(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.locator("#firstName").click()
        self.page.keyboard.type("Ebrahim Hossain")
        time.sleep(2)

    def test_insert_text(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.locator("#firstName").click()
        self.page.keyboard.insert_text("Ebrahim Hossain")
        time.sleep(2)

    def test_key_combinations(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.locator("#firstName").click()
        self.page.keyboard.insert_text("Ebrahim Hossain")
        time.sleep(2)

        # COPY & Paste
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Control+C")
        time.sleep(2)
        self.page.locator("#lastName").click()
        self.page.keyboard.press("Control+V")
        time.sleep(2)

    def test_key_combinations_tab(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.locator("#firstName").click()
        self.page.keyboard.insert_text("Ebrahim Hossain")
        time.sleep(2)

        # COPY & Paste
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Control+C")
        time.sleep(2)
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Control+V")
        time.sleep(2)

    def test_backspace_key(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.locator("#firstName").click()
        self.page.keyboard.insert_text("Ebrahim Hossain")
        time.sleep(2)

        for _ in range(8):
            self.page.keyboard.press("Backspace")

        time.sleep(2)

    def test_delete_key(self):
        self.page.goto(FORM_URL)
        time.sleep(2)
        self.page.locator("#firstName").click()
        self.page.keyboard.insert_text("Ebrahim Hossain")
        time.sleep(2)

        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Delete")

        time.sleep(2)