import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class Test(unittest.TestCase):
    SEARCH_BAR =(By.ID, 'searchboxTrigger')
    SEARCH_BUTTON = (By.XPATH, '//*[@class="em em-search"]')
    ACCEPT_COOKIES = (By.XPATH, '//*[@class ="btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    PRODUCT = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')
    ADD_TO_CART = (By.XPATH, '//*[@class="btn btn-xl btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct"]')
    CLOSE_SUGGESTION = (By.XPATH, '//*[@class = "em em-close gtm_6046yfqs"]')
    CART = (By.XPATH, '//*[@class="jewel jewel-danger"]')
    DELETE_ELEMENT = (By.XPATH, '//*[@class="line-item line-item-footer hidden-xs hidden-sm"]/div[@class="line-footer-action-buttons"]/button[@class="btn btn-link btn-remove-product gtm_rp080219 remove-product"]')
    HOME = (By.XPATH, '//*[@alt="eMAG"]')
    ADD_TO_FAV1 = (By.XPATH, '//*[@class="gtm_t95ovv"]')
    ADD_TO_FAV2_FROM_LIST = (By.XPATH, '//*[@data-productid="53948240"]')
    OPEN_FAV = (By.XPATH, '//*[@id="my_wishlist"]')
    DELETE_ELEMENT_FAV = (By.XPATH, '//*[@class="hidden-sm hidden-xs gtm_9p2y1a"]')
    CLOSE_INTRA_IN_CONT = (By.XPATH, '//*[@class = "js-dismiss-login-notice-btn dismiss-btn btn btn-link pad-sep-none pad-hrz-none"]')
    RESEALED = (By.XPATH, '//*[@title="Resigilate"]')
    RESEALED_PHONE = (By.XPATH, '//*[@href="/cmp/campanie-produse-resigilate-ongoing/telefoane-gadgeturi.php?ref=section_CMP-426208_8323"]')
    ADD_RESEALED_TO_CART = (By.XPATH, '//*[@class="btn btn-default btn-sm btn-block bundle-product-buy-button po-text-small gtm_nhdl6r"]')
    PRODUCT_COUNT_FROM_CART = (By.XPATH, '//*[@id="my_cart"]/span[@class="jewel jewel-danger"]')
    PRODUCTS_IN_CART = (By.XPATH, '//*[@class="mrg-btm-none"]')
    PRODUCT_COUNT_FROM_FAVORITES = (By.XPATH, '//*[@class="products-number hidden-xs js-products-count"]')
    INPUT_NAME = (By.XPATH, '//*[@placeholder="Nume"]')
    INPUT_EMAIL = (By.XPATH, '//*[@placeholder="Email"]')
    MESSAGE_SUBSCRIPTION = (By.XPATH, '//*[@class="mrg-sep-none alert"]')
    SUBSCRIBE_BUTTON = (By.XPATH, '//*[@class="btn btn-danger btn-block js-recaptcha-button"]')
    NO_NAME_ADDED = (By.XPATH, '//*[@class="form-group col-md-4 has-error"]//span[@class="help-block"]')
    NO_EMAIL_ADDED  = (By.XPATH, '//*[@class="help-block"]')
    HONOR_BRAND = (By.XPATH,'//*[@data-name="Honor"]')
    ORDER_BY = (By.XPATH,'//*[@class="btn btn-sm btn-alt sort-control-btn gtm_ejaugtrtnc"]')
    TYPE_OF_ORDER =(By.XPATH,'//*[@data-sort-dir="asc"]')
    CHOSE_RANDOM_PHONE = (By.XPATH,'//*[@class="card-info"]//a[@aria-label="Product details"]')
    VOUCHER_FIELD = (By.XPATH,'//*[@class="form-control js-voucher-code"]')
    VALIDATE_VOUCHER = (By.XPATH,'//*[@class="em em-right"]')
    STATUS_VOUCHER = (By.XPATH,'//*[@class="vouchers-section"]//div[@class="voucher-error js-voucher-error"]')


    def setUp(self):
        # s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro')
        sleep(1)
        self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_INTRA_IN_CONT).click()
        sleep(1)

    def tearDown(self):
        sleep(5)
        self.chrome.quit()

    def test_add_to_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        number_of_products_in_cart = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_CART).text
        assert number_of_products_in_cart == "1","Error: The product was not added to cart"
        #good


    def test_delete_product_from_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        sleep(1)
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        sleep(1)
        products_in_cart = self.chrome.find_element(*self.PRODUCTS_IN_CART).text
        assert "Cosul tau de cumparaturi nu contine produse. " in products_in_cart, "Error: The product was not removed from the cart"

    def test_use_invalid_voucher_code_in_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        sample_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        generated_string = ''.join(random.choices(sample_str, k=10))
        self.chrome.find_element(*self.VOUCHER_FIELD).send_keys(generated_string)
        self.chrome.find_element(*self.VALIDATE_VOUCHER).click()
        sleep(1)
        status_voucher = self.chrome.find_element(*self.STATUS_VOUCHER).text
        assert "Codul de voucher / card cadou este incorect" in status_voucher, "Error: Voucher is valid"

    def test_without_voucher_code_in_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        self.chrome.find_element(*self.VALIDATE_VOUCHER).click()
        sleep(1)
        status_voucher = self.chrome.find_element(*self.STATUS_VOUCHER).text
        assert "Te rugam sa completezi codul voucherului" in status_voucher, "Error: Voucher was typed."


    def test_add_to_favourites(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_FAV1).click()
        self.chrome.find_element(*self.OPEN_FAV).click()
        numbers_of_products_in_favorites = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_FAVORITES).text
        assert numbers_of_products_in_favorites == "1 produs", "Error: The product was removed from the favorites"

    def test_delete_from_favourites(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys(" Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.ADD_TO_FAV2_FROM_LIST).click()
        self.chrome.find_element(*self.OPEN_FAV).click()
        self.chrome.find_element(*self.DELETE_ELEMENT_FAV).click()
        sleep(1)
        numbers_of_products_in_favorites = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_FAVORITES).text
        assert numbers_of_products_in_favorites == "0 produse", "Error: The product was not removed from the favorites"
        #good

    def test_check_if_product_is_resealed(self):
        self.chrome.find_element(*self.RESEALED).click()
        self.chrome.find_element(*self.RESEALED_PHONE).click()
        self.chrome.find_element(*self.CHOSE_RANDOM_PHONE).click()
        self.chrome.find_element(*self.ADD_RESEALED_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        resealed_status = self.chrome.find_element(By.XPATH, '//*[@class="line-item-title main-product-title"]').text
        assert "RESIGILAT: " in resealed_status, "Error : The product is not released."

    def test_newsletter_subscription_without_name(self):
        self.chrome.find_element(*self.INPUT_EMAIL).send_keys("test1234@yahoo.com")
        self.chrome.find_element(*self.SUBSCRIBE_BUTTON).click()
        subscription_without_success = self.chrome.find_element(*self.NO_NAME_ADDED).text
        assert subscription_without_success == "Acest câmp este necesar", "Error: The name was added corectly"
        #good

    def test_newsletter_subscription_without_email(self):
        self.chrome.find_element(*self.INPUT_NAME).send_keys("TEST10000")
        self.chrome.find_element(*self.SUBSCRIBE_BUTTON).click()
        subscription_without_success = self.chrome.find_element(*self.NO_EMAIL_ADDED).text
        assert subscription_without_success == "Acest câmp este necesar", "Error: The e-mail was added corectly"
        #good

    def test_newsletter_subscription_without_name_and_email(self):
        self.chrome.find_element(*self.SUBSCRIBE_BUTTON).click()
        subscription_without_success1 = self.chrome.find_element(*self.NO_NAME_ADDED).text
        subscription_without_success2 = self.chrome.find_element(*self.NO_EMAIL_ADDED).text
        assert subscription_without_success1 == "Acest câmp este necesar", "Error: The name was added corectly"
        assert subscription_without_success2 == "Acest câmp este necesar", "Error: The e-mail was added corectly"
        #good
    def test_check_ascendent_order(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.ORDER_BY).click()
        self.chrome.find_element(*self.TYPE_OF_ORDER).click()
        sleep(1)
        self.chrome.find_element(*self.HONOR_BRAND).click()
        sleep(2)
        price_list = self.chrome.find_elements(By.XPATH,'//*[@class="product-new-price"]')
        print(price_list)
        price_is_sorted = True
        for i in range(len(price_list)-1):
            for j in range(i+1,len(price_list)):
                if float(price_list[i].text.replace(" Lei","").replace(",",'.')) > float(price_list[j].text.replace(" Lei","").replace(",",'.')):
                    price_is_sorted = False
        assert price_is_sorted == True, "Error: sorting did not work"













