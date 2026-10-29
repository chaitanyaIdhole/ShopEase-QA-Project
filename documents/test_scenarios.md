# Test Scenarios — ShopEase QA Project

**Application Under Test:** SauceDemo / Swag Labs  
**Document Version:** 1.1  
**Status:** Draft

## 1. Purpose

This document lists functional test scenarios for the SauceDemo public demonstration application. Scenarios may be executed manually or automated where supported by the project test suite.

## 2. Test Scenarios

| Scenario ID | Feature | Scenario | Preconditions | Expected Outcome |
|---|---|---|---|---|
| TS01 | Login | Log in with valid demo credentials | Login page is open; valid demo credentials are available | User is redirected to the inventory page |
| TS02 | Login | Log in with an invalid password | Login page is open | Login is rejected and an appropriate error message is displayed |
| TS03 | Cart | Add a product to the cart | User is logged in and inventory is displayed | Selected product is added to the cart and the cart indicator updates |
| TS04 | Cart | Remove a product from the cart | User is logged in and a product has been added to the cart | Selected product is removed from the cart |
| TS05 | Inventory | Sort products by price, low to high | User is logged in and inventory is displayed | Products are ordered by ascending price |
| TS06 | Checkout | Continue with required checkout fields empty | User is logged in, has a product in the cart, and has opened checkout information | Checkout cannot continue and validation feedback is displayed |
| TS07 | Checkout | Complete checkout using valid demo data | User is logged in, has a product in the cart, and has supplied the required checkout information | Order completion confirmation is displayed |
| TS08 | Inventory | Open a product details page | User is logged in and inventory is displayed | The selected product's details match the product selected from inventory |

## 3. Execution Notes

- Use the public demo application: https://www.saucedemo.com/
- Use only the application's publicly provided demo credentials and appropriate sample checkout data.
- Record the actual result and status for every executed scenario.
- Mark scenarios as **Not Run**, **Pass**, **Fail**, or **Blocked** as appropriate.
- Record evidence for failures where possible.
- Do not report a scenario as passed unless it has actually been executed and the expected outcome verified.
- Automation coverage and results must be confirmed from the current Selenium test files and test reports.

## 4. Coverage Limitations

This document defines intended functional coverage. It does not, by itself, prove that every scenario has a corresponding automated test. API testing, database testing, performance testing, and security testing are outside the current execution scope.