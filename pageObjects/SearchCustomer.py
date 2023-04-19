import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class SearchCustomer():
    # Add customer page
    txt_search_email_xpath = "//input[@id='SearchEmail']"
    txt_search_firstName_id = "SearchFirstName"
    txt_search_lastName_id = "SearchLastName"
    btn_search_id = "search-customers"

    tbl_search_results_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def searchEmail(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.txt_search_email_xpath)))
        enter_email.clear()
        enter_email.send_keys(email)
    
    def searchFirstName(self, fname):
        enter_fname = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_search_firstName_id)))
        enter_fname.clear()
        enter_fname.send_keys(fname)

    def searchLastName(self, lname):
        enter_lname = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_search_lastName_id)))
        enter_lname.clear()
        enter_lname.send_keys(lname)

    # total number of rows
    def getNoOfRows(self):
        table_rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)
        return len(table_rows)
        # return len(self.driver.find_element(By.XPATH, self.table_rows_xpath))

        # self.no_of_rows = WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, self.table_rows_xpath)))
        # return len(self.no_of_rows)
        
    # total number of columns
    def getNoOfColumns(self):
        no_of_columns = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.table_columns_xpath)))
        return len(self.no_of_columns)

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
        flag = False
        for r in range(1, self.getNoOfRows() +1):
            table =  WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.table_xpath)))
            name = table.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text

            if name == Name:
                flag = True
                break
        return flag

    def clickOnSearch(self):
        click_search = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.btn_search_id)))
        click_search.click()




    def search_customer_by_name_test(self, name):   
        search_box = self.driver.find_element(By.ID, "SearchFirstName")
        search_box.clear()
        search_box.send_keys(name)
        search_box.submit()

        rows = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.table_xpath)))

        for row in rows:
            customer_name = row.find_element(By.XPATH, ".//td[2]").text
            if customer_name == name:
                return True

        return False
