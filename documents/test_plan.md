# Test Plan — ShopEase QA Project

**Application under test:** SauceDemo / Swag Labs  
**Version:** 1.0  
**Status:** Draft

## 1. Objective
Validate key shopping workflows, record evidence, and report reproducible defects.

## 2. In scope
- Login and authentication feedback
- Product inventory display and sorting
- Add/remove products from cart
- Checkout form validation
- Order completion flow

## 3. Out of scope for initial pass
- Load/performance testing
- Security penetration testing
- Real payment processing
- Private backend/database validation without authorized access

## 4. Test approach
1. Execute manual functional tests.
2. Record actual results and evidence.
3. Report defects only after reproduction and requirement comparison.
4. Automate stable smoke/regression cases with Python, Selenium and PyTest.
5. Add API/database checks only where supported endpoints and authorized test data exist.

## 5. Environment
- Application: https://www.saucedemo.com/
- Browser: Chrome (record exact version when executing)
- OS: Record the actual operating system
- Automation: Python 3.10+, Selenium 4, PyTest

## 6. Entry criteria
- Site is reachable.
- Public demo credentials are available.
- Test environment/browser is ready.

## 7. Exit criteria
- Planned test cases have a recorded status.
- Failures have reproducible steps and evidence.
- Unexecuted/blocked tests are clearly marked.
- No defect is marked fixed/closed without retesting.

## 8. Deliverables
Test cases, execution log, defect reports, automation code, and test run report.
