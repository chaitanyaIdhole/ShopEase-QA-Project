# Test Plan — ShopEase QA Project

**Application Under Test:** SauceDemo / Swag Labs  
**Project Name:** ShopEase QA Portfolio Project  
**Document Version:** 1.1  
**Status:** Draft — pending final documentation review

## 1. Objective

Validate key shopping workflows through manual and automated functional testing. Record test results, maintain reproducible defect reports, and use automated regression tests to check supported application behavior.

## 2. Scope

### 2.1 In Scope

- Login and authentication feedback
- Product inventory display and sorting
- Adding and removing products from the cart
- Cart contents and navigation
- Checkout form validation
- Order completion flow
- Browser-based functional regression testing
- Test execution reporting through PyTest and GitHub Actions

### 2.2 Out of Scope

- Load and performance testing
- Security penetration testing
- Real payment processing
- Private backend or database validation without authorized access
- API testing until a documented and authorized API is confirmed

## 3. Test Approach

1. Review requirements and identify test scenarios.
2. Execute manual functional tests and record actual results.
3. Record reproducible defects with steps, expected results, actual results, and evidence.
4. Automate suitable regression scenarios using Python, Selenium WebDriver, and PyTest.
5. Run automated tests locally and through GitHub Actions.
6. Review test reports and investigate failures before marking tests as passed.
7. Add API or database tests only when supported interfaces, authorization, and suitable test data are available.

## 4. Test Environment

- **Application:** https://www.saucedemo.com/
- **Browser:** Google Chrome; record the version for each relevant execution environment.
- **Operating system:** Windows for local execution; Ubuntu GitHub-hosted runner for CI, when applicable.
- **Programming language:** Python.
- **Automation tools:** Selenium WebDriver and PyTest.
- **CI tool:** GitHub Actions.
- **Test data:** Public demo credentials and non-sensitive sample checkout information.

The application is a public demonstration environment used for QA practice. ShopEase is the portfolio project name, not a claim that the team owns or operates SauceDemo.

## 5. Entry Criteria

- The demo application is reachable.
- Public demo credentials are available.
- The browser and required automation dependencies are installed.
- Test cases and expected outcomes are documented.
- The test environment is ready for execution.

## 6. Exit Criteria

- Planned test cases have a recorded execution status.
- Executed tests have actual results.
- Failures have reproducible steps and supporting evidence where possible.
- Blocked, skipped, and unexecuted tests are clearly identified.
- Automated test results are reviewed.
- A defect is not marked fixed or closed without appropriate retesting.
- The final report distinguishes verified results from pending work.

## 7. Deliverables

- Test plan
- Test scenarios
- Manual test case inventory
- Test execution log
- Bug report template and verified defect reports, if any
- Selenium automation source code
- PyTest and GitHub Actions execution results
- JUnit test report, when successfully generated
- Project README and setup instructions

## 8. Risks and Limitations

- The public demo environment may change or become temporarily unavailable.
- Network delays may affect test execution.
- Browser and driver compatibility may affect automation.
- Public demo behavior may not represent a production e-commerce system.
- API and database coverage remains pending unless an authorized interface is identified.
- CI success must be verified from the actual workflow result and test summary.

## 9. Current Project Status

The project includes Selenium-based UI automation and a GitHub Actions workflow. Checkout tests have passed locally in the latest reported local execution. The exact full-suite and CI test counts should be taken from the latest successful test reports.

API testing and database testing are documented as future work, not completed implementations.

## 10. Completion and Maintenance

Update this document when the test scope, automation, environment, or execution strategy changes. Keep all reported test counts and statuses consistent with the corresponding execution evidence.