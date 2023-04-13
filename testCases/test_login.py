import os
from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from datetime import datetime

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

    #logs data, it will be saved in file
    test_suit_name = '****** Test_Suite_001_Login ******'
    test_case_1 = '****** TC1 - Verifying Login page loaded or not ******'
    test1_case_pass = "****** Pass - Login page loaded successfuly ******"
    test1_case_failed = "****** Fail - Login page not loaded ******" 

    test_case_2 = '****** TC2 - Verify user Login or not ******'
    test2_case_pass = "****** Pass - User Loggedin successfuly ******"
    test2_case_failed = "****** Fail - User Logedin failed ******" 
    end_line = '*******************************************\n'

    def test_loginPageLoaded(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        
        logger.write_log(self.test_suit_name)
        logger.write_log(self.test_case_1)

        act_title = self.driver.title
        # it will fail as wrong title given, screenshot will be created
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            logger.write_log(self.test1_case_pass)
            logger.write_log(self.end_line)

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageLoaded.png")
            self.driver.close()
            logger.write_log(self.test1_case_failed)
            logger.write_log(self.end_line)
            assert False

   
    def test_Login(self, setup ):
        self.driver = setup
        self.driver.get(self.baseURL)
        
        logger.write_log(self.test_suit_name)
        logger.write_log(self.test_case_2)

        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            logger.write_log(self.test2_case_pass)
            logger.write_log(self.end_line)

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error(self.test2_case_failed)
            logger.write_log(self.end_line)
            assert False