import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# To run in Chrome:   pytest -s -v --browser_name=chrome test_parser.py
# To run in Firefox:  pytest -s -v --browser_name=firefox test_parser.py

def pytest_addoption(parser):
    parser.addoption('--language', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test ...")
    browser = webdriver.Chrome(options=options)

    # Для Firefox:
    # fp = webdriver.FirefoxProfile()
    # fp.set_preference("intl.accept_languages", user_language)
    # browser = webdriver.Firefox(firefox_profile=fp)

    yield browser
    browser.quit()
