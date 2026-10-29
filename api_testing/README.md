# API Testing

Start with an inventory of documented/authorized endpoints. SauceDemo is primarily a UI practice app; do not assume a public API is available.

For each confirmed endpoint, record:
- Method and URL
- Authentication and test data requirements
- Expected status code
- Response schema and key field assertions
- Negative cases, boundary cases, and cleanup
- Environment and evidence

Do not probe private endpoints or use real credentials/payment information. A Postman collection can be added once a supported API is selected.
