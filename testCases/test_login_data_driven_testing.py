import os
from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from datetime import datetime
from utilities import excelReader
import time
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

# data driven testing
# data is readed from Excel file
class Test_002_DDT_Login:
    baseURL = ReadConfig().getAppURL()
    # excel file path
    path = ".//testData/testData.xlsx"

    #logs data, it will be saved in file
    test_suit_name = '****** Test_Suite_002_Login ******'
    test_case_1 = '****** TC1 - Verifying user Loggedin with valid data or not ******'
    test1_case_pass = "****** Pass - User Loggedin successfuly ******"
    test1_case_failed = "****** Fail - User Logedin failed ******" 
    end_line = '*******************************************\n'

    def test_Login_DDT(self, setup ):
        self.driver = setup
        self.driver.get(self.baseURL)
        logger.write_log(self.test_suit_name)
        logger.write_log(self.test_case_1)

        self.lp = loginPage(self.driver)
        # reading data from excel file
        self.rows = excelReader.getRowCount(self.path, "Sheet1" )
        print("No. of rows in excel file: ", self.rows)

        first_status = []   #empty list variable

        # reading data from excel file
        for r in range(2, self.rows + 1):
            self.user = excelReader.readData(self.path, "Sheet1",r,1)
            self.passwrd = excelReader.readData(self.path, "Sheet1",r,2)
            self.expectedResult = excelReader.readData(self.path, "Sheet1",r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.passwrd)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expectedResult == "Pass":
                    logger.write_log(self.test1_case_pass)
                    logger.write_log(self.end_line)
                    self.lp.clickLogout()
                    first_status.append("Pass")
                elif self.expectedResult == "Fail":
                    logger.write_log(self.test1_case_failed)
                    logger.write_log(self.end_line)
                    self.lp.clickLogout()
                    first_status.append("Fail")
            
            elif act_title != exp_title:
                if self.expectedResult == "Pass":
                    logger.write_log(self.test1_case_failed)
                    logger.write_log(self.end_line)
                    first_status.append("Fail")
                elif self.expectedResult == "Fail":
                    logger.write_log(self.test1_case_pass)
                    logger.write_log(self.end_line)
                    first_status.append("Pass")

        # checking the first_status list whether it meets our criteria or not
            if "Fail" not in first_status:
                logger.write_log(self.test1_case_pass)
                logger.write_log(self.end_line)
                self.driver.close()
                assert True
            else:
                logger.write_log(self.test1_case_failed)
                logger.write_log(self.end_line)
                self.driver.close()
                assert False
