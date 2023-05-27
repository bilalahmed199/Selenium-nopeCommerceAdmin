import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class SearchCustomer():
    # Add customer page
    txt_search_email_xpath = "//input[@id='SearchEmail']"
    txt_search_firstName_xpath = "//input[@id='SearchFirstName']"
    txt_search_lastName_xpath = "//input[@id='SearchLastName']"
    btn_search_id = "search-customers"

    tbl_search_results_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//*[@id='customers-grid']/tbody/tr"
    table_columns_xpath = "//*[@id='customers-grid_wrapper']/div[1]/div/div/div[1]/div/table/thead/tr/th"

    def __init__(self,driver):
        self.driver = driver

    def enterEmail(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.txt_search_email_xpath)))
        enter_email.clear()
        enter_email.send_keys(email)
    
    def enterFirstName(self, fname):
        enter_fname = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.txt_search_firstName_xpath)))
        enter_fname.clear()
        enter_fname.send_keys(fname)

    def enterLastName(self, lname):
        enter_lname = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.txt_search_lastName_xpath)))
        enter_lname.clear()
        enter_lname.send_keys(lname)

    def getNoOfRows(self):
        rows = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.table_rows_xpath)))
        return len(rows)
        
    # total number of columns
    def getNoOfColumns(self):
        columns = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.table_columns_xpath)))
        return len(columns)

    # to search customer bu Email
    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() +1):
            table = self.driver.find_element(By().XPATH,self.table_xpath)

            # table =  WebDriverWait(self.driver, 10).until(
            # expected_conditions.presence_of_element_located((By.XPATH, self.table_xpath)))
            emailID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text

            if emailID == email:
                flag = True
                break
        return flag

    # to search customer bu Name
    def searchCustomerByName(self, Name):
        
        # Verify data from table
        value_found = False
        for r in range(1, self.getNoOfRows() + 1):
            for c in range(1, self.getNoOfColumns() + 1):
                # it will read complete data from Table dynamically
                value = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]"))).text
                # uncomment below line to print the table result found in Console 
                # print(value, end="          ")
                # Check if the value matches
                if value == Name:       # Name will be passed a value in test_searchCustomer class
                    value_found = True
                    break  # Exit the loop if value is found

            # Break the outer loop if value is found
            if value_found:
                break

        # Verify if the value is found or not
        if value_found:
            print(value, "is found on the webpage.")
        else:
            # raise an error explicitely
            raise AssertionError(value, "is not found on the webpage.")

    def clickOnSearch(self):
        click_search = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.btn_search_id)))
        click_search.click()

    # to refresh the Webpage
    # it is done incase an element is overlapped or not found
    def refreshPage(self):
        self.driver.refresh()
