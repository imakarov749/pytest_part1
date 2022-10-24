from selene import be
from selene.support.shared import browser


def open_main_page():
    browser.open('https://github.com/')
    browser.element('[class$=flex-order-2]').should(be.visible)


def click_sign_in_button_desktop():
    browser.element('.HeaderMenu-link--sign-in').click()


def click_toggle_navigation_button():
    browser.element('.Button-label').click()


def click_sign_in_button_mobile():
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()


def close_desktop_browser():
    browser.close_current_tab()


def close_mobile_browser():
    browser.close()
