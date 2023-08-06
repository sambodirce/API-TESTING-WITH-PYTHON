# CoinDesk API Test Suite

This repository contains a test suite for the CoinDesk API, organized using best practices for readability, maintainability, and efficient testing. The test suite is written in Python using the `pytest` framework.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sambodirce/API-TESTING-WITH-PYTHON.git
   cd API-TESTING-WITH-PYTHON
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run tests using pytest command
   ```bash
   pytest


## Organized Test Structure
The test suite is organized using a class-based structure for improved readability and maintainability. Each test class corresponds to a specific aspect of testing the CoinDesk API. The test methods within each class focus on testing individual features.

## Explanation
The organized test structure enhances readability and promotes best testing practices:

* **Reuse of Setup**: The common setup, such as sending a request to the API and parsing the JSON response, is performed once and shared among the test methods. This ensures efficient test execution.

* **Direct Assertions**: The use of direct assertions (without try-except blocks) aligns with pytest's assertion-based approach. Failures are reported clearly, and the tests are easier to understand.

* **Clarity**: The test class and method names are clear and descriptive, conveying the intent and behavior of each test.

## Contributing
Contributions to enhance and expand this test suite are welcome! If you'd like to contribute, please follow the standard GitHub workflow: fork the repository, make your changes, and submit a pull request.
