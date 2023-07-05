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
    DELETE_ELEMENT = (By.XPATH, '//*[@id="cart-products"]/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/div[2]/button')
    HOME = (By.XPATH, '//*[@id="masthead"]/div/div/div[1]/a/img')
    ADD_TO_FAV1 = (By.XPATH, '//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[3]/button/span')
    ADD_TO_FAV2_FROM_LIST = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[2]/button[1]/i')
    OPEN_FAV = (By.XPATH, '//*[@id="my_wishlist"]/span[1]')
    DELETE_ELEMENT_FAV = (By.XPATH, '//*[@class="hidden-sm hidden-xs gtm_9p2y1a"]')
    CAT_LAP_TEL_TAB = (By.XPATH, '//*[@data-modified = "1681819469"]')
    TEL = (By.XPATH, '//*[@id="emg-body-overlay"]/div[2]/div[2]/div/div[3]/aside/ul[1]/li[2]/a')
    IOS = (By.XPATH, '//*[@id="emg-widget-carousel3014"]/div/div/figure[1]/div/a/img')
    LIVRATE_EMAG = (By.XPATH, '//*[@data-option-id="30"]')
    SECTOR = (By.XPATH, '//*[@data-option-id= "11"]')
    IN_STOCK = (By.XPATH, '//*[@data-option-id="stock"]')
    RANGE_PRET = (By.XPATH, '//*[@data-option-id="4000-5000"]')
    IPHONE_14 = (By.XPATH, '//*[@id="js-filter-9396-collapse"]/div/a[2]')
    CLICK_TELEFON = (By.XPATH,'//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')
    ADD_TO_CART2 = (By.XPATH, '//*[@class="btn btn-xl btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct"]')
    CLOSE_SUGGESTION3 = (By.XPATH, '//*[@class="em em-close gtm_6046yfqs"]')
    CLOSE_COOKIE = (By.XPATH, '/html/body/div[13]/div/div[2]/button[1]')
    CLOSE_INTRA_IN_CONT = (By.XPATH, '/html/body/div[13]/div/button/i')


    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro')

    def tearDown(self) -> None:
        sleep(10000)
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
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        sleep(1)
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        sleep(1)
        self.chrome.find_element(*self.HOME).click()

    def test_add_to_fav(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys(" Husa Iphone 14 Pro")
        self.chrome.find_element(*self.GO_TO_RESULT).click()
        sleep(3)
        self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        self.chrome.find_element(*self.PRODUCT).click()
        sleep(1)
        self.chrome.find_element(*self.ADD_TO_FAV1).click()
        sleep(1)
        self.chrome.find_element(*self.HOME).click()
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("incarcator Iphone 14 Pro")
        self.chrome.find_element(*self.GO_TO_RESULT).click()
        sleep(1)
        self.chrome.find_element(*self.ADD_TO_FAV2_FROM_LIST).click()
        sleep(1)
        self.chrome.find_element(*self.HOME).click()
        sleep(1)
        self.chrome.find_element(*self.OPEN_FAV).click()
        sleep(1)
        self.chrome.find_element(*self.DELETE_ELEMENT_FAV).click()
        sleep(1)
        self.chrome.find_element(*self.DELETE_ELEMENT_FAV).click()
        sleep(1)
        self.chrome.find_element(*self.HOME).click()

    def test_search_for_a_product(self):
        self.chrome.find_element(*self.CAT_LAP_TEL_TAB).click()
        sleep(1)
        self.chrome.find_element(*self.TEL).click()
        sleep(1)
        self.chrome.find_element(*self.IOS).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_COOKIE).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_INTRA_IN_CONT).click()
        sleep(1)
        self.chrome.find_element(*self.LIVRATE_EMAG).click()
        sleep(1)
        self.chrome.find_element(*self.SECTOR).click()
        sleep(1)
        self.chrome.find_element(*self.IN_STOCK).click()
        sleep(1)
        self.chrome.find_element(*self.RANGE_PRET).click()
        sleep(1)
        self.chrome.find_element(*self.IPHONE_14).click()
        sleep(1)
        self.chrome.find_element(*self.CLICK_TELEFON).click()
        sleep(1)
        self.chrome.find_element(*self.ADD_TO_CART2).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION3).click()
        sleep(1)
        self.chrome.find_element(*self.CART).click()
        sleep(1)
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        sleep(1)
        self.chrome.find_element(*self.HOME).click()

    def test_oferte_emag(self):









