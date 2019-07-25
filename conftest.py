import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru or en-gb")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('w3c', False)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.implicitly_wait(5)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield driver
    print("\nquit browser..")
    driver.quit()
