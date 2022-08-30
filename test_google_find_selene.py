from selene.support.shared import browser
from selene import have
import pytest

@pytest.fixture()
def configure_window_size():
    browser.config.window_width = 640
    browser.config.window_height = 480

@pytest.fixture()
def configure_max_window_size():
    browser.driver.maximize_window()

def test_find_selene_positive(configure_window_size):
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_find_selene_negative(configure_max_window_size):
    browser.element('[name="q"]').clear().type('seline').press_enter()
    browser.element('[id="search"]').should_not(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))