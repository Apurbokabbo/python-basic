import pytest
from playwright.sync_api import sync_playwright, expect

SUPPORTED_BROWSERS = ["firefox", "chromium", "edge"]

BROWSER_NAME = "chromium"
HEADLESS = False

URL = "https://automation.ebrahimhossain.com.bd/hovers.html"


@pytest.fixture(scope="class")
def setup(request):
    playwright = sync_playwright().start()
    playwright.selectors.set_test_id_attribute("data-test-id")

    match BROWSER_NAME:
        case "chromium":
            browser = playwright.chromium.launch(
                headless=HEADLESS
            )

        case "edge":
            browser = playwright.chromium.launch(
                channel="msedge",
                headless=HEADLESS
            )

        case "firefox":
            browser = playwright.firefox.launch(
                headless=HEADLESS
            )

        case _:
            raise ValueError(f"Browser {BROWSER_NAME} is not supported.")

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )

    page = context.new_page()
    page.goto(URL)

    request.cls.page = page

    yield

    context.close()
    browser.close()
    playwright.stop()


@pytest.mark.usefixtures("setup")
class TestMouseHover:

    @pytest.fixture(autouse=True)
    def reset_mouse_position(self):
        yield
        if hasattr(self, "page"):
            self.page.mouse.move(0, 0)
            self.page.wait_for_timeout(300)

    def test_mouse_hover_example(self):
        service = self.page.get_by_role("button", name="Services")
        expect(service).to_be_visible()

        service.hover()

        consulting = self.page.get_by_role("button", name="Consulting")
        expect(consulting).to_be_visible()
        consulting.hover()

        qa_audit = self.page.get_by_role("link", name="QA Automation Audit")
        expect(qa_audit).to_be_visible()
        qa_audit.click()

    def test_mouse_hover_example2(self):
        category = self.page.get_by_role("button", name="Explore Categories")
        expect(category).to_be_visible()

        category.hover()

        electronics = self.page.get_by_role("button", name="Electronics")
        expect(electronics).to_be_visible()
        electronics.hover()

        audio = self.page.get_by_role("button", name="Audio")
        expect(audio).to_be_visible()
        audio.hover()

        earbuds = self.page.get_by_role("link", name="Wireless Earbuds")
        expect(earbuds).to_be_visible()
        earbuds.click()

    def test_mouse_hover_example3(self):
        security = self.page.get_by_text("Hover to Authenticate")
        expect(security).to_be_visible()

        security.hover()

        token = self.page.get_by_text("SECRET_API_TOKEN_99")
        expect(token).to_be_visible(timeout=10000)

    def test_mouse_hover_example4(self):
        progress = self.page.get_by_test_id("progress-trigger")
        percent = self.page.locator("#progress-percent")

        expect(progress).to_be_visible()

        progress.hover()

        expect(percent).to_have_text("100%", timeout=5000)