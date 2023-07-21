import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_class.base_class import Base


class Cart_Page(Base):

    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    cart_button = "(//span[text()='Добавить в корзину'])[2]"
    shopping_cart = "//*[@id='basketContent']/div[3]/a/span"
    shopping_cart_text = "//span[@class='good-info__good-name']"


    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_shopping_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart)))

    def get_shopping_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_text)))

    # Actions


    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_shopping_cart(self):
        self.get_shopping_cart().click()
        print("Click shopping cart")



    #Methods

    def product_cart(self):


        self.click_cart()
        self.click_shopping_cart()
        self.assert_word(self.get_shopping_cart_text(),'Набор посуды/Cковородок EasyKeep4DG/4D-4предмета')








