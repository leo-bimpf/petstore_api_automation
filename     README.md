# Petstore API Automation

This is a simple API automation project written in Python using pytest and requests.

## Stack
- Python 3.12
- pytest
- requests
- Allure Reports

## Project structure

- clients/ — API clients
- config/ — settings (base url, headers)
- tests/ — test cases
- conftest.py — fixtures

## How to run tests

```bash
pytest -v --alluredir=allure-results