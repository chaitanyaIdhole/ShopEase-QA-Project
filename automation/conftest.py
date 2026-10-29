
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """Start Chrome for a test and always close it afterward."""
    options = Options()

    # Required for headless browser execution in GitHub Actions
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,1000")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)

    try:
        yield browser
    finally:
        browser.quit()
