from pageObjects.LoginPage import loginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageLoaded(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_Login(self, setup ):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = loginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        self.driver.close()

# testing git push
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:

            assert False