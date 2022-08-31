import pytest
from selene.support.shared import browser

@pytest.fixture(scope="session", autouse=True)
def open_browser():
    browser.open('https://www.google.com/ncr')
    yield

@pytest.fixture()
def configure_window_size():
    browser.config.window_width = 640
    browser.config.window_height = 480

@pytest.fixture()
def configure_max_window_size():
    browser.driver.maximize_window()
