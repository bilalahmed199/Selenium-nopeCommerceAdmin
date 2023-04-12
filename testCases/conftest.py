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

# ******* Pytest HTML reports *********
# it is hook for adding environment info to HTML report
def pytest_configure(config):
    # below info is added explicitly to be shown in the HTML report
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Bilal'
    

# it is hook to delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # below info is deleted explicitly to not be shown in the HTML report
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)
