from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    else:
        driver = webdriver.Ie()
    return driver

# This will get value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return Browser value to the Setup function
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Pytest HTML reports
# This is a hook for adding environment info to the HTML report
def pytest_configure(config):
    # Below info is added explicitly to be shown in the HTML report
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Bilal'


# This is a hook to delete/modify environment info in the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Below info is deleted explicitly to not be shown in the HTML report
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)
    return metadata