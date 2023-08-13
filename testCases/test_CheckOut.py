import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import Login
from pageObjects.CheckOutPage import CredKart_CheckOut


class Test_CredKart_CheckOut:

    def test_checkout(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Click_Login_link()
        self.lp.Enter_Email("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.CLick_Login_Button()
        self.cop = CredKart_CheckOut(self.driver)
        # Click on Product--Macbook
        self.cop.Click_MacBook()
        # Click on add to cart
        self.cop.Click_Add_Cart()
        # Proceed to Checkout
        self.cop.Click_Proceed_ToCheckout()
        time.sleep(3)
        # Enter First_Name
        self.cop.Enter_First_Name("Tushar")
        # Enter Last_Name
        self.cop.Enter_Last_Name("K")
        # Enter Phone
        self.cop.Enter_Phone("9091929355")
        # Enter Address
        self.cop.Enter_Address("Dhankawdi, Pune")
        # Enter Zip
        self.cop.Enter_Zip("411013")
        # Select state
        self.cop.DropDown_State("Pune")
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
        self.cop.Get_Order_Number()
        if self.lp.Login_Status() == True:
            assert True
        else:
            assert False
