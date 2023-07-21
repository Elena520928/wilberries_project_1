import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_class.base_class import Base


class Main_Page(Base):

    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    products = "//*[@id='app']/div[2]/div/div[3]/div[1]/div/ul[1]/li[2]/div/div/a/div/img"
    menu_button = "//button[@class='nav-element__burger j-menu-burger-btn j-wba-header-item hide-mobile']"
    house_button = "//a[@class='menu-burger__main-list-link menu-burger__main-list-link--258']"
    kitchen_button = "//a[@href='/catalog/dom-i-dacha/kuhnya']"
    pan_button = "//a[@href='/catalog/dom-i-dacha/kuhnya/kastryuli-i-skovorody']"
    pan_title_check = "(//span[@itemprop='name'])[4]"
    brand_button = "(//button[@data-link='{on toggleDesktopDropdown}text{:model.name}'])[5]"
    check_box_button = "(//span[@class ='checkbox-with-text__text'])[4]"
    ready_button = "//button[@class='filter-btn__main btn-main j-close-dropdown-OTY0ZWU0OTItZWRiNS0xZjNmLTY3NTAtZDZjOGFkZjQwN2E0']"
    product_1 = "//*[@id='c45847826']/div/a"


    # Getters
    def get_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.products)))
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_house_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house_button)))

    def get_kitchen_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.kitchen_button)))

    def get_pan_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pan_button)))

    def get_pan_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pan_title_check)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_button)))

    def get_check_box_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_button)))

    def get_ready_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ready_button)))


    # Actions

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click menu button")

    def click_house_button(self):
        self.get_house_button().click()
        print("Click house button")

    def click_kitchen_button(self):
        self.get_kitchen_button().click()
        print("Click kitchen button")

    def click_pan_button(self):
        self.get_pan_button().click()
        print("Click pan button")

    def click_brand_button(self):
        self.get_brand_button().click()
        print("Click brand button")

    def click_check_box_button(self):
        self.get_check_box_button().click()
        print("Click check_box button")

    def click_check_box_button_return(self):
        self.get_check_box_button().send_keys(Keys.RETURN)
        print("Click check_box button return")

    def click_ready_button(self):
        self.get_ready_button().click()
        print("Click ready button")

    def click_select_products(self):
        self.get_products().click()
        print("Click select products")

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Click select product 1")


    #Methods

    def select_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_menu_button()
        self.click_house_button()
        self.click_kitchen_button()
        self.click_pan_button()
        self.assert_word(self.get_pan_title(), 'Кастрюли и сковороды')
        self.click_brand_button()
        self.click_check_box_button()
        self.click_brand_button()
        self.click_select_product_1()









