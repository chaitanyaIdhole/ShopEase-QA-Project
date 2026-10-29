
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"



def open_checkout_information_page(driver):
    driver.get(BASE_URL)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys(USERNAME)

    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "1"
        )
    )

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "checkout"))
    ).click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )




def open_checkout_information_page(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys(USERNAME)

    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Confirm that login reached the inventory page.
    wait.until(EC.url_contains("inventory.html"))

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Add a product and verify the cart badge.
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "1"
        )
    )

    # Open the cart.
    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    wait.until(EC.url_contains("cart.html"))

    # Click Checkout only after the cart page is ready.
    
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )

    ActionChains(driver) \
        .move_to_element(checkout_button) \
        .click() \
        .perform()

    # Confirm that the checkout form actually appears.
    wait.until(EC.url_contains("checkout-step-one.html"))

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )



def test_checkout_requires_first_name(driver):
    open_checkout_information_page(driver)

    # Leave all checkout fields empty.
    driver.find_element(By.ID, "continue").click()

    error = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )
    assert "First Name is required" in error.text


def test_checkout_requires_last_name(driver):
    open_checkout_information_page(driver)

    driver.find_element(By.ID, "first-name").send_keys("Chaitanya")
    # Leave last name and postal code empty.
    driver.find_element(By.ID, "continue").click()

    error = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )
    assert "Last Name is required" in error.text


def test_checkout_requires_postal_code(driver):
    open_checkout_information_page(driver)

    driver.find_element(By.ID, "first-name").send_keys("Chaitanya")
    driver.find_element(By.ID, "last-name").send_keys("Idhole")
    # Leave postal code empty.
    driver.find_element(By.ID, "continue").click()

    error = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )
    assert "Postal Code is required" in error.text


def test_successful_checkout_displays_confirmation(driver):
    open_checkout_information_page(driver)

    driver.find_element(By.ID, "first-name").send_keys("Chaitanya")
    driver.find_element(By.ID, "last-name").send_keys("Idhole")
    driver.find_element(By.ID, "postal-code").send_keys("411001")
    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.ID, "checkout_summary_container")
        )
    )

    driver.find_element(By.ID, "finish").click()

    confirmation = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )
    assert "Thank you for your order" in confirmation.text
