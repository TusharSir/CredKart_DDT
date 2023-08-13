import pytest

from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator


class Test_CredKart_Login:
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_pageTitle_001(self, setup):
        self.driver = setup
        ####### log level example ################
        self.log.debug("this is debug")
        self.log.info("this is info")
        self.log.warning("this is warning")
        self.log.error("this is error")
        self.log.critical("this is critical")
        ####################################################
        self.log.info("Started testcase test_pageTitle_001")
        self.log.info("Opening the the browser")
        self.log.info("Checking the Page title:- " + self.driver.title)
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\ScreenSHots\\test_pageTitle_001_pass.PNG")
            self.log.info("Taking the screenshot")
            self.driver.close()
            self.log.info("Testcase test_pageTitle_001 is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenSHots\\test_pageTitle_001_fail.PNG")
            self.log.info("Taking the screenshot")
            self.driver.close()
            self.log.info("Testcase test_pageTitle_001 is failed")
            assert False
        self.log.info("Testcase test_pageTitle_001 is completed")

    @pytest.mark.sanity
    def test_CredKart_Login_002(self, setup):
        self.driver = setup
        self.log.info("Started testcase test_CredKart_Login_002")
        self.log.info("Opening browser")
        self.lp = Login(self.driver)
        self.lp.Click_Login_link()
        self.log.info("Click on login link")
        # self.driver.get("https://automation.credence.in/login")
        self.lp.Enter_Email("Credencetest@test.com")
        self.log.info("Entering Email ")
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.log.info("Entering Password")
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        self.lp.CLick_Login_Button()
        self.log.info("Click on login button")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # print(self.lp.Login_Status())
        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(".\\ScreenShots\\test_CredKart_Login_002_pass.PNG")
            self.log.info("Taking screenshot")
            self.log.info("Testcase test_CredKart_Login_002 is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_CredKart_Login_002_fail.PNG")
            self.log.info("Taking screenshot")
            self.log.info("Testcase test_CredKart_Login_002 is Failed")
            assert False
        self.log.info("Testcase test_CredKart_Login_002 is Completed")

# pytest -v -s --html=Reports/myreport.html --alluredir="allure-results" -n=2  testCases/test_CheckOut_ddt.py --browser chrome
# testcases
# Cross Browser -- with changing code, now we change the browser with command line
# Metadata for html report pytest-metadata
# Parameterized (Test Data) testcases
# Page objects --> we are defining the all the activities/operations
# Data Driven testing with openpyxl (Excel sheet Test Data)
# logging object -->

# pytest -m "markername" -- > this will run the testcases having given marker name
# example pytest -m "sanity"--> this will run only the sanity marker testcases
# example pytest -m "sanity and regression"--> this will run only the sanity and regression both marker testcases
# example pytest -m "sanity or regression"--> this will run the testcases either having marker sanity or  regression.


# Today's task :
# How to remove warning from console output, search command for it ?
# How to register marker in pytest (https://docs.pytest.org/en/stable/how-to/mark.html) ?


# CT#15 --> sunday monday no class
# CT#14 --> class HR session
# From Tuesday --> we're going start the framework from scratch with theory notes
