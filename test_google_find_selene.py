from selene.support.shared import browser
from selene import have

def test_find_selene_positive(configure_window_size):
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('[aria-label="Page 2"]').click()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_find_selene_negative(configure_max_window_size):
    browser.element('[name="q"]').clear().type('seline').press_enter()
    browser.element('[id="search"]').should_not(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))