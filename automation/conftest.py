
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):
    """Start Chrome and capture diagnostic details when a test fails."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,1000")

    options.set_capability(
    "goog:loggingPrefs",
    {"browser": "ALL"}
)

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)

    yield browser

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports", exist_ok=True)

        print(f"\nFailed test: {request.node.nodeid}")
        print(f"Current URL: {browser.current_url}")
        print(f"Page title: {browser.title}")
        print("PAGE TEXT:", browser.find_element("tag name", "body").text[:5000])

        print("INPUTS:", browser.execute_script("""
            return Array.from(document.querySelectorAll("input")).map(
                e => ({
                    id: e.id,
                    name: e.name,
                    placeholder: e.placeholder,
                    type: e.type
                })
            )
        """))

        print("BUTTONS:", browser.execute_script("""
            return Array.from(document.querySelectorAll("button")).map(
                e => ({
                    id: e.id,
                    text: e.innerText,
                    dataTest: e.getAttribute("data-test")
                })
            )
        """))

        print("BROWSER CONSOLE LOGS:")
        for entry in browser.get_log("browser"):
            print(entry)

        screenshot = os.path.join(
            "reports",
            request.node.name + ".png"
        )
        browser.save_screenshot(screenshot)
        print(f"Screenshot saved: {screenshot}")

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
