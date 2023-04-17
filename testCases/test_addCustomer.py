from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from datetime import datetime
from Constants import constants
from pageObjects.AddNewCustPage import AddNewCustomer
from utilities.customLogger import Logger 
import string
import random
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig().getAppURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getUserPassword()

    # add customer with valid data
    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        
        # to capture logs in log file
        log_file_path = './Logs/automation.log'  # specify the path of the log file
        self.logger = Logger(log_file_path)
        self.logger.write_log(constants.test_suite_003)
        self.logger.write_log(constants.TS3_test_case_1)
        self.driver.maximize_window()

        # login user from LoginPage class
        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # data from AddNewCustPage class
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItems()
        self.addcust.clickOnAddNew()

        # to generate random email everytime
        # self.email = random_generator() + "@gmail.com"
        # self.addcust.enterEmail(self.email)
        # self.addcust.enterPassword("abc123")
        # self.addcust.enterFirstName("Bilal")
        # self.addcust.enterLastName("Test")
        # self.addcust.selectGender("Male")
        # self.addcust.enterDOB("07/07/2000")
        # self.addcust.enterCompanyName("Test Company")
        self.addcust.enterNewsletter("Test")
        self.addcust.selectIsTaxExempt()
        self.addcust.selectRole("Vendors")
        self.addcust.clickOnSave()

        # this will save the message shown on the screen in text
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.write_log(constants.TS3_TC1_pass)
            self.logger.write_log(constants.end_line)
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.write_log(constants.TS3_TC1_failed)
            self.logger.write_log(constants.end_line)
            assert False == False
        self.driver.close()






# to generate random data of 8 charactors string
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) 



