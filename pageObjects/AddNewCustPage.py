import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class AddNewCustomer:
    linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuItem_xpath = "(//p[contains(text(),'Customers')])[2]"
    btn_addNew_xpath = "//a[@class='btn btn-primary']"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_firstName_id = "FirstName"
    txt_lastName_id = "LastName"
    rd_genderMale_id = "Gender_Male"
    rd_genderFemale_id = "Gender_Female"
    txt_dob_id = "DateOfBirth"
    txt_company_id = "Company"
    rd_IsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    list_newsletter_xpath = "(//div[@role='listbox'])[1]"
    select_newsletter_xpath = "//li[normalize-space()='Test store 2']"
    list_custRoles_xpath = "(//div[@role='listbox'])[2]"
    list_listItemRegistered_xpath = "//li[normalize-space()='Registered']"
    list_listItemAdministrators_xpath = "//li[normalize-space()='Administrators']"
    list_listItemGuests_xpath = "//li[normalize-space()='Guests']"
    list_listItemVendors_xpath = "//li[normalize-space()='Vendors']"
    txt_custRoles_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        customers_menu = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.linkCustomers_menu_xpath)))
        customers_menu.click()
    
    def clickOnCustomersMenuItems(self):
        customers_menu_items = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.linkCustomers_menuItem_xpath)))
        customers_menu_items.click()
    
    def clickOnAddNew(self):
        add_new_customer = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.btn_addNew_xpath)))
        add_new_customer.click()

    def enterEmail(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_email_id)))
        enter_email.clear()
        enter_email.send_keys(email)
    
    def enterPassword(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_password_id)))
        enter_password.clear()
        enter_password.send_keys(password)

    def enterFirstName(self, firstName):
        first_name = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_firstName_id)))
        first_name.clear()
        first_name.send_keys(firstName)

    def enterLastName(self, lastName):
        last_name = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_lastName_id)))
        last_name.clear()
        last_name.send_keys(lastName)

    def selectGender(self, gender):
        if gender == "Male":
            element_id = self.rd_genderMale_id
        elif gender == "Female":
            element_id = self.rd_genderFemale_id
        else:
            element_id = self.rd_genderMale_id

        WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, element_id))).click()

    def enterDOB(self, dob):
        enter_DOB = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_dob_id)))
        enter_DOB.clear()
        enter_DOB.send_keys(dob)

    def enterCompanyName(self, companyName):
        company_name = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_company_id)))
        company_name.clear()
        company_name.send_keys(companyName)
  
   # click on newsletter list, search by text & select result
    def enterNewsletter(self, newsletter):
        enter_newsletter = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_newsletter_xpath)))
        enter_newsletter.click()

        WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, self.select_newsletter_xpath))).click()
    
    def selectIsTaxExempt(self):
        is_tax_exampt = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.rd_IsTaxExempt_xpath)))
        is_tax_exampt.click()

    def selectRole(self, role):
        select_role = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.list_custRoles_xpath)))
        select_role.click()

        if role == "Registered":
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemRegistered_xpath)))
        elif role == "Administrators":
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemAdministrators_xpath)))

        elif role == "Guests":
            # we can only either select Registered or Guest as role
            # test will fail in this case as we will select both Guests & Registered
            select_role.click()
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemGuests_xpath)))
        
        elif role == "Registered":
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemRegistered_xpath)))
        elif role == "Vendors":
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemVendors_xpath)))

        else:
            self.listItem = self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemGuests_xpath)))
        # selecting the customer role
        # below line didn't worked, so will use execute_script line 
        # self.listItem.click()
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def clickOnSave(self):
        click_save = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.btn_save_xpath)))
        click_save.click()