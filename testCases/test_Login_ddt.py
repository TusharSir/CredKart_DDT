import pytest

from pageObjects.LoginPage import Login
from utilities import XLutils
from utilities.Logger import LogGenerator


class Test_CredKart_Login_DTT:
    log = LogGenerator.loggen()
    XlPath = "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#14 & " \
             "15\\CredKart_Pytest_Project\\testCases\\TestData\\LoginTest - Copy.xlsx"

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_CredKart_Login_ddt_006(self, setup):
        self.driver = setup  # open browser
        self.log.info("Started testcase test_CredKart_Login_ddt_006")
        self.log.info("Opening browser")
        self.lp = Login(self.driver)  # pageobject call
        self.row = XLutils.RowCount(self.XlPath, "Sheet1")  # xl row count
        # print("Number of rows in excel is " + str(self.row))
        Login_status_List = []
        for r in range(2, self.row + 1):  # iterate xl rows
            self.email = XLutils.ReadData(self.XlPath, "Sheet1", r, 2)  # email read
            self.password = XLutils.ReadData(self.XlPath, "Sheet1", r, 3)  # password read
            self.exp_result = XLutils.ReadData(self.XlPath, "Sheet1", r, 4)  # exp result read
            self.lp.Click_Login_link()
            self.log.info("Click on login link")
            self.lp.Enter_Email(self.email)
            self.log.info("Entering Email:-" + self.email)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering Password:-" + self.password)
            self.lp.CLick_Login_Button()
            self.log.info("Click on Login Button")
            # print(self.lp.Login_Status())
            if self.lp.Login_Status() == True:
                if self.exp_result == "Pass":
                    self.log.info("This case is Pass")
                    Login_status_List.append("Pass")
                    self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
                    self.log.info("Taking screenshot")
                    self.lp.CLick_Menu_Button()
                    self.log.info("Click on Menu button")
                    self.lp.CLick_Logout_Button()
                    self.log.info("Click on Logout button")
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5,"Pass")
                elif self.exp_result == "Fail":
                    self.log.info("This case is Fail")
                    Login_status_List.append("Fail")
                    self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
                    self.log.info("Taking screenshot")
                    self.lp.CLick_Menu_Button()
                    self.log.info("Click on Menu button")
                    self.lp.CLick_Logout_Button()
                    self.log.info("Click on Logout button")
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Fail")
            if self.lp.Login_Status() == False:
                if self.exp_result == "Pass":
                    self.log.info("This case is Fail")
                    Login_status_List.append("Fail")
                    self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
                    self.log.info("taking screenshot")
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Fail")
                elif self.exp_result == "Fail":
                    self.log.info("This case is Pass")
                    Login_status_List.append("Pass")
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Pass")

        self.log.info("Login_status_List-->" + str(Login_status_List))
        print(Login_status_List)
        if "Fail" not in Login_status_List:
            self.log.info("Data driven testcase test_CredKart_Login_ddt_006 is passed")
            assert True
        else:
            self.log.info("Data driven testcase test_CredKart_Login_ddt_006 is Fail")
            assert False
        self.log.info("Data driven testcase test_CredKart_Login_ddt_006 is completed")



# 100s testcases--> if you have to run it in firefox

# pytest -v --html=Reports/myreport.html --alluredir="AllureReports" -n=2  testCases/test_Login.py --browser chrome
