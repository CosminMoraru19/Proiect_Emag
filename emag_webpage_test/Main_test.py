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



class Test(unittest.TestCase):
    SEARCH_BAR =(By.ID, 'searchboxTrigger')
    GO_TO_RESULT = (By.XPATH, '//*[@class="em em-search"]')
    ACCEPT_COOKIES = (By.XPATH, '//*[@class ="btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    PRODUCT = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')
    ADD_TO_CART = (By.XPATH, '//*[@class="btn btn-xl btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct"]')
    CLOSE_SUGGESTION = (By.XPATH, '//*[@class = "em em-close gtm_6046yfqs"]')
    CLOSE_SUGGESTION2 = (By.XPATH, '//*[@class = "em em-close gtm_6046yfqs"]')
    CART = (By.XPATH, '//*[@id="my_cart"]/span[2]')
    CONTINUE_FROM_CART = (By.XPATH, '//*[@class = " btn btn-emag btn-secondary font-size-md btn-block btn-lg gtm_sn11312018"]')
    INSERT_EMAIL = (By.XPATH, '//*[@name = "user_login[email]"]')
    CONTINUA = (By.XPATH, '//*[@id = "user_login_continue"]')
    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro')

    def tearDown(self) -> None:
        sleep(1000)
        self.chrome.quit()

    def test_add_to_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys(" Husa Iphone 14 Pro")
        self.chrome.find_element(*self.GO_TO_RESULT).click()
        sleep(3)
        self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        self.chrome.find_element(*self.PRODUCT).click()
        sleep(3)
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(3)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        sleep(1)
        self.chrome.find_element(*self.CART).click()
        self.chrome.find_element(*self.SEARCH_BAR).send_keys(" incarcator Iphone 14 Pro")
        self.chrome.find_element(*self.GO_TO_RESULT).click()
        sleep(3)
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION2).click()
        sleep(1)
        self.chrome.find_element(*self.CART).click()
        sleep(1)
        self.chrome.find_element(*self.CONTINUE_FROM_CART).click()
        sleep(1)
        self.chrome.find_element(*self.INSERT_EMAIL).send_keys('cosminmoraru1996@gmail.com')
        sleep(1)
        self.chrome.find_element(*self.CONTINUA).click()
        sleep(5)
        self.chrome.back()

