import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class loginPage:
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"
    btn_logout_xpath = "(//a[normalize-space()='Logout'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.txtbox_username_id).clear()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txtbox_username_id))).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.txtbox_password_id).clear()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txtbox_password_id))).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()
