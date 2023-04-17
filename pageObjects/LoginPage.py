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
        set_username = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txtbox_username_id)))
        set_username.clear()
        set_username.send_keys(username)

    def setPassword(self,password):
        set_password = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.txtbox_password_id)))
        set_password.clear()
        set_password.send_keys(password)

    def clickLogin(self):
        click_login = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.btn_login_xpath)))
        click_login.click()

    def clickLogout(self):
        click_logout = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.btn_logout_xpath)))
        click_logout.click()

