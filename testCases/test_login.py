from pageObjects.LoginPage import loginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageLoaded(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        # it will fail as wrong title given, screenshot will be created
        if act_title == "Your store. Loginnasdad":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageLoaded.png")
            self.driver.close()
            assert False

    def test_Login(self, setup ):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()

            assert False