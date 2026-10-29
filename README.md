# ShopEase QA Automation Project

## Overview
ShopEase QA is a web UI test automation project built using Python, Selenium WebDriver, and Pytest. It tests key shopping workflows on the SauceDemo demo application.

## Tech Stack
- Python 3.12
- Selenium WebDriver
- Pytest
- Google Chrome
- Git and GitHub

## Automated Test Coverage

### Login
- Valid login
- Invalid password
- Empty credentials
- Locked-out user

### Products and Cart
- Product inventory is displayed
- Expected product count is verified
- Add-to-cart badge is updated
- Added product appears in the cart

### Checkout
- Checkout information page opens
- First name is required
- Last name is required
- Postal code is required
- Successful checkout displays order confirmation

## Test Results
Latest recorded run: **12 passed, 0 failed**

Execution time: 148.90 seconds.

These results reflect one successful local run. Execution time and results may vary between runs.

## Prerequisites
- Python 3.12 or compatible version
- Google Chrome
- Git (for version control)

## Setup Instructions

1. Clone this repository.
2. Open the project directory.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it on Windows PowerShell:
   `.venv\Scripts\Activate.ps1`
5. Install dependencies:
   `python -m pip install -r requirements.txt`
6. Run the test suite:
   `python -m pytest`

Selenium Manager may automatically manage the appropriate ChromeDriver version, subject to browser and network availability.

## Demo Application
https://www.saucedemo.com/

## Project Structure

```text
ShopEase-QA-Project/
├── automation/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_products.py
│   └── test_checkout.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Disclaimer
This project is for educational and portfolio purposes. It uses a public demo shopping application and does not process real customer orders.