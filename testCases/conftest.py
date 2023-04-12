from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    else: 
        driver = webdriver.Ie()
    return driver

# this will get value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# this will return Browser value to Setup function
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")