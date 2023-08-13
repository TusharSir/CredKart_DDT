import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CredKart_CheckOut:
    Click_Product_MacBook_XPATH = (By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3")
    Click_AddToCart_XPATH = (By.XPATH, "//input[@value='Add to Cart']")
    Click_ProceedToCheckOut_XPATH = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    Enter_First_Name_XPATH = (By.XPATH, "//input[@id='first_name']")
    Enter_Last_Name_XPATH = (By.XPATH, "//input[@id='last_name']")
    Enter_Phone_XAPTH = (By.XPATH, "//input[@id='phone']")
    Enter_Address_XAPTH = (By.XPATH, "//textarea[@id='address']")
    Enter_Zip_XPATH = (By.XPATH, "//input[@id='zip']")
    DropDown_State_XPATH = (By.XPATH, "//select[@id='state']")
    Enter_Owner_Name_XPATH = (By.XPATH, "//input[@id='owner']")
    Enter_CVV_XPATH = (By.XPATH, "//input[@id='cvv']")
    DropDown_Year_XPATH = (By.XPATH, "//select[@id='exp_year']")
    DropDown_Month_XPATH = (By.XPATH, "//select[@id='exp_month']")
    Enter_Card_Number_XPATH = (By.XPATH, "//input[@id='cardNumber']")
    Click_Continue_Checkout_XPATH = (By.XPATH, "//button[@id='confirm-purchase']")
    Success_Message = (By.XPATH, "/html/body/div/div[1]/p[1]")
    Order_Number_CSS = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)")
    Click_HomePage_XPATH = (By.XPATH, "//a[@class='navbar-brand']")

    def __init__(self, driver):
        self.driver = driver

    def Click_MacBook(self):
        self.driver.find_element(*CredKart_CheckOut.Click_Product_MacBook_XPATH).click()

    def Click_Add_Cart(self):
        self.driver.find_element(*CredKart_CheckOut.Click_AddToCart_XPATH).click()

    def Click_Proceed_ToCheckout(self):
        self.driver.find_element(*CredKart_CheckOut.Click_ProceedToCheckOut_XPATH).click()

    def Enter_First_Name(self, firstname):
        self.driver.find_element(*CredKart_CheckOut.Enter_First_Name_XPATH).send_keys(firstname)

    def Enter_Last_Name(self, lastname):
        self.driver.find_element(*CredKart_CheckOut.Enter_Last_Name_XPATH).send_keys(lastname)

    def Enter_Phone(self, phone):
        self.driver.find_element(*CredKart_CheckOut.Enter_Phone_XAPTH).send_keys(phone)

    def Enter_Address(self, address):
        self.driver.find_element(*CredKart_CheckOut.Enter_Address_XAPTH).send_keys(address)

    def Enter_Zip(self, zip):
        self.driver.find_element(*CredKart_CheckOut.Enter_Zip_XPATH).send_keys(zip)

    def Enter_Owner(self, owner):
        self.driver.find_element(*CredKart_CheckOut.Enter_Owner_Name_XPATH).send_keys(owner)

    def Enter_CVV(self, cvv):
        self.driver.find_element(*CredKart_CheckOut.Enter_CVV_XPATH).send_keys(cvv)

    def Enter_CardNumber(self, cardnumber):
        self.driver.find_element(*CredKart_CheckOut.Enter_Card_Number_XPATH).send_keys(cardnumber)

    def dropdown_Year(self, year):
        Year = Select(self.driver.find_element(*CredKart_CheckOut.DropDown_Year_XPATH))
        Year.select_by_visible_text(year)

    def dropdown_month(self, month):
        Month = Select(self.driver.find_element(*CredKart_CheckOut.DropDown_Month_XPATH))
        Month.select_by_visible_text(month)

    def DropDown_State(self, statename):
        state = Select(self.driver.find_element(*CredKart_CheckOut.DropDown_State_XPATH))
        state.select_by_visible_text(statename)

    def Click_Continue_Checkout(self):
        self.driver.find_element(*CredKart_CheckOut.Click_Continue_Checkout_XPATH).click()

    def Order_status(self):
        try:
            OrderNumber = self.driver.find_element(*CredKart_CheckOut.Order_Number_CSS)
            return True
        except NoSuchElementException:
            return False

    def Get_Order_Number(self):
        try:
            OrderNumber = self.driver.find_element(*CredKart_CheckOut.Order_Number_CSS).text
            return OrderNumber
        except NoSuchElementException:
            pass


    def Click_HomePage(self):
        self.driver.find_element(*CredKart_CheckOut.Click_HomePage_XPATH).click()
