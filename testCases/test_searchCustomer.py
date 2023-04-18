from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from datetime import datetime
from Constants import constants
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.AddNewCustPage import AddNewCustomer
from utilities.customLogger import Logger 
from selenium.webdriver.common.by import By
import time

class Test_004_SearchCustomer:
    baseURL = ReadConfig().getAppURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getUserPassword()

    # add customer with valid data
    def test_searchCustByEmail(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        
        # to capture logs in log file
        log_file_path = './Logs/automation.log'  # specify the path of the log file
        self.logger = Logger(log_file_path)
        self.logger.write_log(constants.test_suite_004)
        self.logger.write_log(constants.TS4_test_case_1)
        self.driver.maximize_window()

        # login user from LoginPage class
        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # data from AddNewCustPage class, Go to Search customer page
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItems()

        # data from SearchCustomer class, Search customer by email
        searchcust = SearchCustomer(self.driver)
        searchcust.searchEmail("bilaltest@test.com")
        searchcust.clickOnSearch()
        time.sleep(3)

        custFound = self.driver.find_element(By().XPATH, "//td[normalize-space()='Bilal Test']")
        print(custFound.text)
        if custFound.text == "Bilal Test":
            assert True
            self.logger.write_log(constants.TS4_TC1_pass)
            self.logger.write_log(constants.end_line)
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchCustomer.png")
            self.logger.write_log(constants.TS4_TC1_failed)
            self.logger.write_log(constants.end_line)
            assert False
            


        # status = searchcust.searchCustomerByEmail("bilaltest@test.com")
        # if status == "bilaltest@test.com":
        #     self.logger.write_log(constants.TS4_TC1_pass)
        #     self.logger.write_log(constants.end_line)
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_searchCustomer.png")
        #     self.logger.write_log(constants.TS4_TC1_failed)
        #     self.logger.write_log(constants.end_line)
        #     assert False

