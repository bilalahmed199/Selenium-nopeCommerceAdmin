import os
from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from datetime import datetime
from Constants import constants

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def write_log(self, log_message):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f'{current_time} - {log_message}\n')

log_file_path = './Logs/automation.log'  # specify the path of the log file
logger = Logger(log_file_path)

class Test_001_Login:
    baseURL = ReadConfig().getAppURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getUserPassword()

    def test_loginPageLoaded(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        
        logger.write_log(constants.test_suite_001)
        logger.write_log(constants.TS1_test_case_1)

        act_title = self.driver.title
        # it will fail as wrong title given, screenshot will be created
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            logger.write_log(constants.TS1_TC1_pass)
            logger.write_log(constants.end_line)

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageLoaded.png")
            self.driver.close()
            logger.write_log(constants.TS1_TC1__failed)
            logger.write_log(constants.end_line)
            assert False

   
    def test_Login(self, setup ):
        self.driver = setup
        self.driver.get(self.baseURL)
        
        logger.write_log(constants.test_suite_001)
        logger.write_log(constants.TS1_test_case_2)

        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            logger.write_log(constants.TS1_TC2_pass)
            logger.write_log(constants.end_line)

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error(constants.TS1_TC2_failed)
            logger.write_log(constants.end_line)
            assert False