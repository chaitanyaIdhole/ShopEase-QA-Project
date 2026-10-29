from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_valid_login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    assert "inventory" in driver.current_url


def test_invalid_password_shows_error(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys("incorrect-demo-password")
    driver.find_element(By.ID, "login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert error.is_displayed()



def test_empty_credentials_show_error(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert error.is_displayed()
    assert "Username is required" in error.text



def test_locked_out_user_cannot_login(driver):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys(
        "locked_out_user"
    )
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert error.is_displayed()
    assert "locked out" in error.text.lower()
