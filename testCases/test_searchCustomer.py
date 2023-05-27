from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from datetime import datetime
from Constants import constants
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.AddNewCustPage import AddNewCustomer
from utilities.customLogger import Logger 
from selenium.webdriver.common.by import By
import time, string, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_004_SearchCustomer:
    baseURL = ReadConfig().getAppURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getUserPassword()

    # add customer with valid data
    def test_searchCustByEmail(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        # to capture logs in log file
        log_file_path = './Logs/automation.log'  # specify the path of the log file
        self.logger = Logger(log_file_path)
        self.logger.write_log(constants.test_suite_004)
        self.logger.write_log(constants.TS4_test_case_1)

        # login user from LoginPage class
        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # data from AddNewCustPage class, Add customer to search
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItems()
        
        ## uncomment below code when script is ran for the 1st time
        ## coz db is clear on this demo site after 24 hours
        # # so will have to create the new customer once, so that it could be searched  
        self.addcust.clickOnAddNew()
        self.email = random_generator() + "@bilaltasdest.com"
        self.addcust.enterEmail(self.email)
        self.addcust.enterPassword("abc123")
        self.addcust.enterFirstName("Bilal")
        self.addcust.enterLastName("Test")
        self.addcust.selectGender("Male")
        self.addcust.clickOnSave()

        # data from SearchCustomer class, Search customer by email
        searchcust = SearchCustomer(self.driver)
        searchcust.enterEmail("@bilaltasdest.com")
        searchcust.clickOnSearch()

        # Getting current URL source code
        get_source = self.driver.page_source
 
        # Text you want to search
        search_text = "Bilal Test"
        if search_text in get_source:
            self.logger.write_log(constants.TS4_TC1_pass)
            self.logger.write_log(constants.end_line)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchCustomerByEmail.png")
            self.logger.write_log(constants.TS4_TC1_failed)
            self.logger.write_log(constants.end_line)
            self.driver.quit()
            assert False


    def test_searchCustByName(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        # to capture logs in log file
        log_file_path = './Logs/automation.log'  # specify the path of the log file
        self.logger = Logger(log_file_path)
        self.logger.write_log(constants.test_suite_004)
        self.logger.write_log(constants.TS4_test_case_2)

        # login user from LoginPage class
        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # data from AddNewCustPage class, Add customer to search
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItems()

        # data from SearchCustomer class, Search customer by Name
        searchcust = SearchCustomer(self.driver)
        # searchcust.refreshPage()
        searchcust.enterFirstName("John")
        searchcust.enterLastName("Smith")
        searchcust.clickOnSearch()

        # Wait for the element to be visible
        wait = WebDriverWait(self.driver, 10)

        # wrong xpath is given to fail the test
        element_present = wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//td[text()='Johns Smith']"), "John Smith"))

        # Verify if the customer is found or not based on element presence
        if element_present:
            self.logger.write_log(constants.TS4_TC2_pass)
            self.logger.write_log(constants.end_line)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchCustomerByName.png")
            self.logger.write_log(constants.TS4_TC2_failed)
            self.logger.write_log(constants.end_line)
            self.driver.quit()
            assert False
            

# to generate random data of 8 charactors string
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) 