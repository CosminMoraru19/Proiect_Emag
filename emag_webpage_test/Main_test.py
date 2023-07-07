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
    CLOSE_COOKIE = (By.XPATH, '//*[@class = "btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    CLOSE_INTRA_IN_CONT = (By.XPATH, '//*[@class = "js-dismiss-login-notice-btn dismiss-btn btn btn-link pad-sep-none pad-hrz-none"]')
    OFERTE_EMAG = (By.XPATH, '//*[@title = "Ofertele eMAG"]')
    HOME_DEALS = (By.XPATH, '//*[@src = "https://s13emagst.akamaized.net/layout/ro/images/db/104/156523.jpg?width=768&height=768&hash=DD6A30DBF728F09082F15DEABCDF0A6A"]')
    PISCINE = (By.XPATH,'//*[@src="https://s13emagst.akamaized.net/layout/ro/images/db//104/156364.jpg"]')
    RATEING =(By.XPATH, '//*[@data-option-id="5-5"]')
    PISCINA = (By.XPATH, '//*[@alt="Piscina Bestway Steel Pro MAX, pompa filtrare, 4.27m x 84cm"]')
    RESIGILATE = (By.XPATH, '//*[@title="Resigilate"]')
    TELEFOANE_RESIGILATE = (By.XPATH, '//*[@href="/cmp/campanie-produse-resigilate-ongoing/telefoane-gadgeturi.php?ref=section_CMP-426208_8323"]')
    TELEFON_SAMSUNG = (By.XPATH,'//*[@href="/telefon-mobil-samsung-galaxy-s22-dual-sim-128gb-8gb-ram-5g-phantom-black-sm-s901bzkdeue/pd/DTZ01FMBM/?ref=prod_CMP-426208_8323_92538#used-products"]')
    ADD_SAM_CART = (By.XPATH,'//*[@class="btn btn-default btn-sm btn-block bundle-product-buy-button po-text-small gtm_nhdl6r"]')
    GOTOMAG = (By.XPATH,'//*[@id="cart-products"]/div/div[1]/div[3]/div/div/p/a')
    TELEFOANE_MOBILE = (By.XPATH, '//*[@href="/telefoane-mobile/c?tree_ref=13&ref=cat_tree_93"]')
    PRIMUL_TELEFOM = (By.XPATH,'//*[@src="https://s13emagst.akamaized.net/products/54129/54128719/images/res_1ead99862ad5ddaa2dd84e4bef27361f.jpg?width=720&height=720&hash=A195069FC7B4A97398EB1E46EFD2BC4E"]')
    APPLE = (By.XPATH, '//*[@data-name="Apple"]')
    CLOSE_ADD = (By.XPATH,'/html/body/div[1]/div/div/button/i')
    OPEN_APPLE_PRODUCT = (By.XPATH,'//*[@src="https://s13emagst.akamaized.net/products/48592/48591225/images/res_88dbb52d3570c8fd119fe82ad975b680.jpg?width=720&height=720&hash=049B4E257BDEB2E40207DABE3041A31D"]')

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
        self.chrome.find_element(*self.OFERTE_EMAG).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_COOKIE).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_INTRA_IN_CONT).click()
        sleep(1)
        self.chrome.find_element(*self.HOME_DEALS).click()
        sleep(1)
        self.chrome.find_element(*self.PISCINE).click()
        sleep(1)
        self.chrome.find_element(*self.LIVRATE_EMAG).click()
        sleep(1)
        self.chrome.find_element(*self.IN_STOCK).click()
        sleep(1)
        self.chrome.find_element(*self.RATEING).click()
        sleep(1)
        self.chrome.find_element(*self.PISCINA).click()
        sleep(1)
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        sleep(1)
        self.chrome.find_element(*self.CART).click()
        sleep(1)
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        sleep(1)
        self.chrome.find_element(*self.HOME).click()

    def test_resigilate(self):
        self.chrome.find_element(*self.RESIGILATE).click()
        sleep(1)
        self.chrome.find_element(*self.TELEFOANE_RESIGILATE).click()
        sleep(1)
        self.chrome.find_element(*self.TELEFON_SAMSUNG).click()
        sleep(1)
        self.chrome.find_element(*self.ADD_SAM_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        sleep(1)
        self.chrome.find_element(*self.CART).click()
        Element = self.chrome.find_element(By.XPATH, '//*[@id="cart-products"]/div/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/a/span')
        Element_cautat = 'RESIGILAT'
        if Element_cautat in Element.text:
            print('Telefonul este de la resigilate')
            self.chrome.find_element(*self.CONTINUE_FROM_CART).click()
            self.chrome.find_element(*self.INSERT_EMAIL).send_keys("cosminmoraru1996@gmail.com")
            self.chrome.find_element(*self.CONTINUA).click()
            self.chrome.back()
            self.chrome.find_element(*self.HOME).click()
        else:
            print('Telefonul nu este resigilat')
            self.chrome.find_element(*self.DELETE_ELEMENT).click()
            sleep(1)
            self.chrome.find_element(*self.GOTOMAG).click()

    def test_nume_telefon_corect(self):
        self.chrome.find_element(*self.CAT_LAP_TEL_TAB).click()
        sleep(1)
        self.chrome.find_element(*self.TEL).click()
        sleep(1)
        self.chrome.find_element(*self.TELEFOANE_MOBILE).click()
        sleep(1)
        self.chrome.find_element(*self.PRIMUL_TELEFOM).click()
        ELEMENT1 = self.chrome.find_element(By.XPATH,'//*[@class="page-title"]').text
        print(ELEMENT1)
        ELEMENT2DECAUTAT = "Telefon mobil Apple iPhone 14 Pro, 128GB, 5G, Deep Purple"
        if ELEMENT2DECAUTAT in ELEMENT1:
            print('Ai gasit telefonul dorit')
            self.chrome.find_element(*self.ADD_TO_CART).click()
        else:
            self.chrome.back()
            sleep(1)
            self.chrome.find_element(*self.CLOSE_COOKIE).click()
            sleep(1)
            self.chrome.find_element(*self.CLOSE_INTRA_IN_CONT).click()
            sleep(1)
            self.chrome.find_element(*self.APPLE).click()
            sleep(1)
            self.chrome.find_element(*self.CLOSE_ADD).click()
            sleep(1)
            self.chrome.find_element(*self.OPEN_APPLE_PRODUCT).click()
            sleep(1)
            ELEMENT2 = self.chrome.find_element(By.XPATH, "//*[@class='page-title']").text
            print(ELEMENT2)
            if ELEMENT2DECAUTAT in ELEMENT2:
                print('Ai gasit telefonul dorint de tine')
                self.chrome.find_element(*self.ADD_TO_CART).click()
                sleep(1)
                self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
                sleep(1)
                self.chrome.find_element(*self.HOME).click()
            else:
                print('Nu ai gasit telefonul dorit')
















