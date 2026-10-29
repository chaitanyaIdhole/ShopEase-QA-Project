# ShopEase QA Automation Project

A portfolio project demonstrating web UI test automation using Python, Selenium WebDriver, and PyTest against the public SauceDemo demonstration application.

> **Application under test:** SauceDemo / Swag Labs  
> **Project type:** QA automation and testing portfolio  
> **Status:** In progress

## Overview

This project demonstrates functional testing of common e-commerce workflows, including login, product inventory, shopping cart operations, and checkout validation.

It combines automated browser tests with manual test documentation and a GitHub Actions workflow.

**Important:** ShopEase is the name of this portfolio project. SauceDemo is the external demonstration application being tested.

## Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Google Chrome
- Git and GitHub
- GitHub Actions

## Automated Test Coverage

### Login

- Valid login
- Invalid password
- Empty credentials
- Locked-out user

### Products and Shopping Cart

- Product inventory display
- Product count verification
- Add-to-cart behavior and cart badge
- Verification that an added product appears in the cart

### Checkout

- Checkout information page navigation
- Required first-name validation
- Required last-name validation
- Required postal-code validation
- Successful checkout confirmation

The list above describes the intended or previously documented coverage. Refer to the current test files and test reports to confirm the exact tests included in each run.

## Test Results

A previously reported local test run completed with **12 passed and 0 failed** in approximately **148.90 seconds**.

This is a historical result, not a claim about the latest execution. Test counts and execution time can change when tests or the environment change.

To verify the current result, run the suite locally or check the latest GitHub Actions workflow summary.

## Project Structure

```text
ShopEase-QA-Project/
├── .github/
│   └── workflows/
│       └── pytest.yml
├── automation/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_products.py
│   └── test_checkout.py
├── api_testing/
│   └── README.md
├── bug_reports/
│   └── BUG_TEMPLATE.md
├── documents/
│   ├── test_plan.md
│   └── test_scenarios.md
├── reports/
│   └── README.md
├── test_cases/
│   ├── execution_log.csv
│   └── manual_test_cases.csv
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10 or compatible version supported by the installed dependencies
- Google Chrome
- Git, if cloning the repository
- Internet access to reach the demo application and download required browser-driver components when necessary

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/chaitanyaIdhole/ShopEase-QA-Project.git
cd ShopEase-QA-Project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the automated tests

```bash
python -m pytest
```

### 6. Generate a JUnit test report

Create the reports directory if it does not exist:

```bash
python -c "from pathlib import Path; Path('reports').mkdir(exist_ok=True)"
```

Then run:

```bash
python -m pytest --junitxml=reports/junit-results.xml
```

Selenium Manager may automatically manage the appropriate ChromeDriver version, depending on browser compatibility, network availability, and environment configuration.

## Continuous Integration

The GitHub Actions workflow is located at `.github/workflows/pytest.yml`.

It is configured to run the automated tests on repository pushes, pull requests, and manual workflow dispatches.

Check the **Actions** tab in the GitHub repository for the actual workflow status, test summary, and any available report artifacts.

A green workflow indicates that the configured job completed successfully. Always review the test summary to confirm the number of tests that passed, failed, or were skipped.

## Manual Testing and Documentation

The repository also contains:

- A test plan and functional test scenarios
- A manual test case inventory
- A test execution log
- A reusable bug report template
- API testing documentation describing scope and limitations

Manual test cases should be marked as passed or failed only after execution. No defect should be reported as confirmed without reproducible evidence.

## Scope and Limitations

- Testing targets the public SauceDemo demonstration application.
- This project does not own or operate the application under test.
- No real customer orders or payments are processed.
- API and database testing are not claimed as implemented without a confirmed, authorized interface.
- Performance and security penetration testing are outside the current scope.
- Test results depend on the application, browser, network, and execution environment.

## Future Improvements

- Add explicit waits and reusable page objects where appropriate.
- Improve test failure diagnostics and screenshot capture.
- Expand positive and negative test coverage.
- Maintain traceability between scenarios, manual cases, automation, and results.
- Review and improve CI reporting.

## Disclaimer

This project is intended for educational and portfolio purposes. SauceDemo is used as a public demonstration application for practicing software quality assurance and browser automation.