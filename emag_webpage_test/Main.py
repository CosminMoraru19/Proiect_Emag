import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Initializa_pagina import Test


class Test(unittest.TestCase):
    SEARCH_BAR =(By.ID, 'searchboxTrigger')
    GO_TO_RESULT = (By.XPATH, '//*[@class="em em-search"]')
    ACCEPT_COOKIES = (By.XPATH, '//*[@class ="btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    PRODUCT = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')
    CHOSE_MEMORY1 = (By.XPATH, '//*[@id="product_colors"]/li[1]/a/div')
    ADD_TO_CART = (By.XPATH, '//*[@class="btn btn-xl btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct"]')
    CLOSE_WARANTY = (By.XPATH, '//*[@class="em em-close gtm_6046yfqs"]')
    CONTUL_MEU = (By.XPATH,'//*[@id="my_account"]/i')
    ADRESA_EMAIL = (By.XPATH, '//*[@id="user_login_email"]')
    BUTON_CONTINUE = (By.XPATH, '//*[@id="user_login_continue"]')
    PAROLA_EMAIL = (By.XPATH, '//*[@id="user_login_email"]')
    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro')

    def tearDown(self) -> None:
        sleep(1000)
        self.chrome.quit()

    def test_add_to_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Iphone 14 Pro")
        self.chrome.find_element(*self.GO_TO_RESULT).click()
        sleep(3)
        self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        self.chrome.find_element(*self.PRODUCT).click()
        sleep(1)
        # self.chrome.find_element(*self.CHOSE_MEMORY1).click()
        sleep(1)
        self.chrome.find_element(*self.ADD_TO_CART).click()
        self.chrome.find_element(*self.CLOSE_WARANTY).click()

    def test_log_in(self):
        self.chrome.find_element(*self.CONTUL_MEU).click()
        sleep(1)
        self.chrome.find_element(*self.ADRESA_EMAIL).send_keys('cosminmoraru1996@gmail.com')
        sleep(1)
        self.chrome.find_element(*self.BUTON_CONTINUE).click()
        sleep(1)








