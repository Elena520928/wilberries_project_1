import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_class.base_class import Base


class Address_Page(Base):

    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    address_button = "/html/body/div[1]/main/div[2]/div/div[2]/div/div[1]/form/div[1]/div[2]/div[2]"
    search_input_address = "(//input[@class='ymaps-2-1-79-searchbox-input__input'])[1]"
    select_address = "(//span[text()='г Балашиха, Улица Кожедуба 6'])[1]"
    search_button = "(//ymaps[text()='Найти'])[1]"
    select_button = "//button[text()='Выбрать']"
    check_address = "//*[@id='basketForm']/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div/span[1]"


    # Getters

    def get_address_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_button)))

    def get_search_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_input_address)))

    def get_select_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_address)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_select_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button)))

    def get_check_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_address)))


    # Actions


    def click_address_button(self):
        self.get_address_button().click()
        print("Click address_button")

    def search_input(self):
        self.get_search_input().send_keys("г Балашиха, Улица Кожедуба 6")
        print("Input address")

    def click_search_button_action(self):
        self.get_search_button().click()
        print("Click Search")

    def select_address_string(self):
        self.get_select_address_field().click()
        print("Select address")

    def click_select_button_action(self):
        self.get_select_button().click()
        print("Click select button")

    #Methods

    def select_address_method(self):


        self.click_address_button()
        self.search_input()
        self.click_search_button_action()
        self.select_address_string()
        self.click_select_button_action()
        self.assert_word(self.get_check_address(),'г Балашиха, Улица Кожедуба 6,')
        self.get_screenshot()
        self.assert_url('https://www.wildberries.ru/lk/basket')








