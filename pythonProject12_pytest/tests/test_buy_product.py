import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.address_page import Address_Page
from pages.cart_page import Cart_Page
from pages.main_page import Main_Page



class Test_1():

    def test_buy_product(self):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service('C:\\Users\\ALEX\\PycharmProjects\\pythonSelenium\\chromedriver.exe', chrome_options = options)
        driver = webdriver.Chrome(service=service)

        print("Start Test")

        mp = Main_Page(driver)
        mp.select_product()
        cp = Cart_Page(driver)
        cp.product_cart()
        address = Address_Page(driver)
        address.select_address_method()


        time.sleep(10)



