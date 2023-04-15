import time
from selenium.webdriver.support.ui import Select

class AddNewCustomer:
    linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuItem_xpath = "(//p[contains(text(),'Customers')])[2]"
    btn_addNew_xpath = "//a[@class='btn btn-primary']"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_firstName_id = "FirstName"
    txt_lastName_id = "LastName"
    rd_gender_id = "Gender_Male"
    txt_dob_id = "DateOfBirth"
    txt_company_id = "Company"
    rd_IsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txt_newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
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
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.linkCustomers_menu_xpath))).click()

    def clickOnCustomersMenuItems(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.linkCustomers_menuItem_xpath))).click()
    
    def clickOnAddNew(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.btn_addNew_xpath))).click()

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.id, self.txt_email_id))).send_keys(email)
    
    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.id, self.txt_password_id))).send_keys(password)

    def enterFirstName(self, firstName):
        self.driver.find_element(By.ID, self.txt_firstName_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.id, self.txt_firstName_id))).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element(By.ID, self.txt_lastName_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.id, self.txt_lastName_id))).send_keys(lastName)
    
    def selectGender(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.rd_gender_id))).click()

    def enterDOB(self, dob):
        self.driver.find_element(By.ID, self.txt_dob_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_dob_id))).send_keys(dob)

    def enterCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.txt_company_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_company_id))).send_keys(companyName)
  
   # click on newsletter list, search by text & select result
    def enterNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.list_newsletter_xpath).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_newsletter_xpath))).send_keys(newsletter)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.select_newsletter_xpath))).click()
   
    def enterCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.txt_company_id).clear()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txt_company_id))).send_keys(companyName)
    
    def selectIsTaxExempt(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.rd_IsTaxExempt_xpath))).click()

    def selectRole(self, role):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_custRoles_xpath))).click()
        
        if role == "Registered":
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemRegistered_xpath)))
        elif role == "Administrators":
            self.listItem = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.list_listItemAdministrators_xpath)))

        elif role == "Guests":
            # we can only either select Registered or Guest as role
            # removing Registered as it is selected by default
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
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








