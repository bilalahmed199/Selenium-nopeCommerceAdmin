from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig 
from utilities.customLogger import LogGenerator

class Test_001_Login:
    baseURL = ReadConfig().getAppURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getUserPassword()

    logger = LogGenerator().log_generator()

    def test_loginPageLoaded(self,setup):
        self.logger.info("****** Test_001_Login ******")
        self.logger.info("****** Verifying Login page loaded or not ******")

        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        # it will fail as wrong title given, screenshot will be created
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("****** Login page loaded successfuly ******")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageLoaded.png")
            self.driver.close()
            self.logger.error("****** Login page not loaded ******")
            assert False

   
    # def test_Login(self, setup ):
    #     self.logger.info("****** Test_001_Login******")
    #     self.logger.info("****** Verifying user Loggedin with valid data or not ******")
        
    #     self.driver = setup
    #     self.driver.get(self.baseURL)

    #     self.lp = loginPage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()

    #     act_title = self.driver.title
    #     if act_title == "Dashboard / nopCommerce administration":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("****** Login test passed ******")

    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
    #         self.driver.close()
    #         self.logger.error("****** Login test failed ******")
    #         assert False