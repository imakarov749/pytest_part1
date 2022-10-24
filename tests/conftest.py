import pytest
from selene import be
from selene.support.shared import browser


# фикстуры для разного разрешения браузеров
@pytest.fixture()
def desktop_config():
    browser.config.window_width = 1080
    browser.config.window_height = 1920


@pytest.fixture()
def mobile_config():
    # разрешение взято для iphone 12pro
    browser.config.window_width = 390
    browser.config.window_height = 844


# фикстуры для пропуска теста при неподходящем разрешении браузера
@pytest.fixture()
def for_skip_mobile_test():
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    if browser.config.window_width > 390 and browser.config.window_height > 844:
        pytest.skip("Установленное соотношение сторон браузера не подходит под мобильную версию")
    else:
        browser.open_url('https://github.com/')
        browser.element('[class$=flex-order-2]').should(be.visible)


@pytest.fixture()
def for_skip_desktop_test():
    browser.config.window_width = 390
    browser.config.window_height = 844
    if browser.config.window_width < 1080 and browser.config.window_height < 1920:
        pytest.skip("Установленное соотношение сторон браузера не подходит под десктопную версию")
    else:
        browser.open_url('https://github.com/')
        browser.element('[class$=flex-order-2]').should(be.visible)


# фикстура для параметризации
@pytest.fixture()
def for_parametrize(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
