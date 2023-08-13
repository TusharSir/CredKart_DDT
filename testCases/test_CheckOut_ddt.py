import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import Login
from pageObjects.CheckOutPage import CredKart_CheckOut
from utilities import XLutils


class Test_CredKart_CheckOut_DDT:
    excel_path = "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#14 & 15\\CredKart_Pytest_Project\\testCases\\TestData\\CheckOutTestData.xlsx"

    def test_checkout_DDT(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Click_Login_link()
        self.lp.Enter_Email("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.CLick_Login_Button()
        self.cop = CredKart_CheckOut(self.driver)
        # Click on Product--Macbook
        Order_Number = []
        self.rows = XLutils.RowCount(self.excel_path, "Sheet1")

        for r in range(2, self.rows + 1):
            self.FirstName = XLutils.ReadData(self.excel_path, "Sheet1", r, 2)
            self.LastName = XLutils.ReadData(self.excel_path, "Sheet1", r, 3)
            self.Phone = XLutils.ReadData(self.excel_path, "Sheet1", r, 4)
            self.Address = XLutils.ReadData(self.excel_path, "Sheet1", r, 5)
            self.Zip = XLutils.ReadData(self.excel_path, "Sheet1", r, 6)
            self.State = XLutils.ReadData(self.excel_path, "Sheet1", r, 7)
            self.Owner = XLutils.ReadData(self.excel_path, "Sheet1", r, 8)

            self.cop.Click_MacBook()
            # Click on add to cart
            self.cop.Click_Add_Cart()
            # Proceed to Checkout
            self.cop.Click_Proceed_ToCheckout()
            time.sleep(3)
            # Enter First_Name
            self.cop.Enter_First_Name(self.FirstName)
            # Enter Last_Name
            self.cop.Enter_Last_Name(self.LastName)
            # Enter Phone
            self.cop.Enter_Phone(self.Phone)
            # Enter Address
            self.cop.Enter_Address(self.Address)
            # Enter Zip
            self.cop.Enter_Zip(self.Zip)
            # Select state
            self.cop.DropDown_State(self.State)
            # state = Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
            # state.select_by_visible_text("Pune")
            # Enter  Owner name
            self.cop.Enter_Owner("Tushar")
            # Enter CVV
            self.cop.Enter_CVV("043")
            # Select Year
            self.cop.dropdown_Year("2024")
            # Select Month
            self.cop.dropdown_month("May")
            # Enter card number
            # 5281 0370 4891 6168
            self.cop.Enter_CardNumber("5281")
            self.cop.Enter_CardNumber("0370")
            self.cop.Enter_CardNumber("4891")
            self.cop.Enter_CardNumber("6168")
            # Click on Checkout button
            self.cop.Click_Continue_Checkout()
            if self.cop.Order_status() == True:
                Order_Number.append(self.cop.Get_Order_Number())
                XLutils.WriteData(self.excel_path, "Sheet1", r, 9, self.cop.Get_Order_Number())
            else:
                pass
            self.cop.Click_HomePage()
        print(len(Order_Number))
        print(Order_Number)
        if len(Order_Number) == (self.rows-1):
            assert True
        else:
            assert False