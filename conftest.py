import pytest
from selene.support.shared import browser

@pytest.fixture(scope="session", autouse=True)
def open_browser():
    browser.open('https://www.google.com/ncr')
    yield
