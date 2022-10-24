import pytest

from model.pages import github_pages


def test_click_sign_in_button_desk(desktop_config):
    github_pages.open_main_page()
    github_pages.click_sign_in_button_desktop()
    github_pages.close_desktop_browser()


def test_click_sign_in_button_mob(mobile_config):
    github_pages.open_main_page()
    github_pages.click_toggle_navigation_button()
    github_pages.click_sign_in_button_mobile()
    github_pages.close_mobile_browser()


def test_skip_mobile_version(for_skip_mobile_test):
    github_pages.click_toggle_navigation_button()
    github_pages.click_sign_in_button_mobile()
    github_pages.close_mobile_browser()


def test_skip_desktop_version(for_skip_desktop_test):
    github_pages.click_sign_in_button_desktop()
    github_pages.close_desktop_browser()


@pytest.mark.parametrize('for_parametrize', [(1080, 1920)], indirect=True)
def test_sign_in_desktop(for_parametrize):
    github_pages.open_main_page()
    github_pages.click_sign_in_button_desktop()
    github_pages.close_desktop_browser()


@pytest.mark.parametrize('for_parametrize', [(390, 844)], indirect=True)
def test_github_mobile(for_parametrize):
    github_pages.open_main_page()
    github_pages.click_toggle_navigation_button()
    github_pages.click_sign_in_button_mobile()
    github_pages.close_mobile_browser()