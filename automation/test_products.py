
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_products_display_after_login(driver):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    assert len(products) == 6, (
        f"Expected 6 products, but found {len(products)}"
    )




def test_add_product_to_cart_updates_badge(driver):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert cart_badge.text == "1"




def test_cart_contains_added_product(driver):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_list")
        )
    )

    product = driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    )

    assert product.text == "Sauce Labs Backpack"
