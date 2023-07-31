import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    SEARCH_BAR =(By.ID, 'searchboxTrigger')
    SEARCH_BUTTON = (By.XPATH, '//*[@class="em em-search"]')
    ACCEPT_COOKIES = (By.XPATH, '//*[@class ="btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    PRODUCT = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')
    ADD_TO_CART = (By.XPATH, '//*[@class="btn btn-xl btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct"]')
    CLOSE_SUGGESTION = (By.XPATH, '//*[@class = "em em-close gtm_6046yfqs"]')
    CART = (By.XPATH, '//*[@class="jewel jewel-danger"]')
    CONTINUE_FROM_CART = (By.XPATH, '//*[@class = " btn btn-emag btn-secondary font-size-md btn-block btn-lg gtm_sn11312018"]')
    INSERT_EMAIL = (By.XPATH, '//*[@name = "user_login[email]"]')
    CONTINUA = (By.XPATH, '//*[@id = "user_login_continue"]')
    DELETE_ELEMENT = (By.XPATH, '//*[@id="cart-products"]/div/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/button')
    HOME = (By.XPATH, '//*[@alt="eMAG"]')
    ADD_TO_FAV1 = (By.XPATH, '//*[@class="gtm_t95ovv"]')
    ADD_TO_FAV2_FROM_LIST = (By.XPATH, '//*[@data-productid="53948240"]')
    OPEN_FAV = (By.XPATH, '//*[@id="my_wishlist"]')
    DELETE_ELEMENT_FAV = (By.XPATH, '//*[@class="hidden-sm hidden-xs gtm_9p2y1a"]')
    CAT_LAP_TEL_TAB = (By.XPATH, '//*[@data-modified = "1681819469"]')
    TEL = (By.XPATH, '//*[@href="/telefoane-mobile-accesorii/sd?tree_ref=12&ref=dep_cat_tree_12"]')
    IOS = (By.XPATH, '//*[@href="/telefoane-mobile/brand/apple/c?ref=subcat_0_prod-type_0"]')
    LIVRATE_EMAG = (By.XPATH, '//*[@data-option-id="30"]')
    SECTOR = (By.XPATH, '//*[@data-option-id= "11"]')
    IN_STOCK = (By.XPATH, '//*[@data-option-id="stock"]')
    RANGE_PRET = (By.XPATH, '//*[@data-option-id="4000-5000"]')
    IPHONE_14 = (By.XPATH, '//*[@id="js-filter-9396-collapse"]/div/a[2]')
    CLICK_TELEFON = (By.XPATH,'//*[@alt="Telefon mobil Apple iPhone 14, 128GB, 5G, Midnight"]')
    ADD_TO_CART2 = (By.XPATH, '//*[@class="btn btn-xl btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct"]')
    CLOSE_SUGGESTION3 = (By.XPATH, '//*[@class="em em-close gtm_6046yfqs"]')
    CLOSE_COOKIE = (By.XPATH, '//*[@class = "btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    CLOSE_INTRA_IN_CONT = (By.XPATH, '//*[@class = "js-dismiss-login-notice-btn dismiss-btn btn btn-link pad-sep-none pad-hrz-none"]')
    RESIGILATE = (By.XPATH, '//*[@title="Resigilate"]')
    TELEFOANE_RESIGILATE = (By.XPATH, '//*[@href="/cmp/campanie-produse-resigilate-ongoing/telefoane-gadgeturi.php?ref=section_CMP-426208_8323"]')
    TELEFON_SAMSUNG = (By.XPATH,'//*[@href="/telefon-mobil-samsung-galaxy-s22-dual-sim-128gb-8gb-ram-5g-phantom-black-sm-s901bzkdeue/pd/DTZ01FMBM/?ref=prod_CMP-426208_8323_92538#used-products"]')
    ADD_SAM_CART = (By.XPATH,'//*[@class="btn btn-default btn-sm btn-block bundle-product-buy-button po-text-small gtm_nhdl6r"]')
    GOTOMAG = (By.XPATH,'//*[@class="mrg-btm-none"]')
    TELEFOANE_MOBILE = (By.XPATH, '//*[@href="/telefoane-mobile/c?tree_ref=13&ref=cat_tree_93"]')
    PRIMUL_TELEFOM = (By.XPATH,'//*[@alt="Telefon mobil Samsung Galaxy A14, Dual SIM, 4GB RAM, 64GB, 4G, Light Green"]')
    APPLE = (By.XPATH, '//*[@data-name="Apple"]')
    OPEN_APPLE_PRODUCT = (By.XPATH,'//*[@src="https://s13emagst.akamaized.net/products/48592/48591225/images/res_88dbb52d3570c8fd119fe82ad975b680.jpg?width=720&height=720&hash=049B4E257BDEB2E40207DABE3041A31D"]')
    TELEFOANE_ACCESORII = (By.XPATH,'//*[@href="/telefoane-mobile-accesorii/sd?tree_ref=12&ref=dep_cat_tree_12"]')
    BATERII = (By.XPATH,'//*[@href="/power-bank-telefoane/c?tree_ref=0&ref=cat_tree_2411"]')
    BATERIE = (By.XPATH,'//*[@id="card_grid"]/div[1]/div/div/div[3]/a/div[1]/img')
    CONTUL_MEU = (By.XPATH, '//*[@id="my_account"]')
    OMITE_LOGIN = (By.XPATH, '//*[@class="button-submit button"]')
    GIFT_CLOSE = (By.XPATH,'//*[@class="close"]')
    ADD_TO_CART3 = (By.XPATH,'//*[@data-pnk="D1PGV6MBM"]')
    PRODUCT_COUNT_FROM_CART = (By.XPATH,'//*[@id="my_cart"]//span[@class="jewel jewel-danger"]')
    PRODUCT_COUNT_FROM_FAVORITES = (By.XPATH, '//*[@class="products-number hidden-xs js-products-count"]')
    PRODUCT_COUNT_FROM_FAVORITES2 = (By.XPATH, '//*[@class="products-number hidden-xs js-products-count"]')
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
        self.chrome.find_element(*self.HOME).click()
        number_of_products_in_cart = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_CART).text
        print(number_of_products_in_cart)
        assert number_of_products_in_cart == "1","Error: The product was not added to cart"


    def test_delete_product_from_cart(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        sleep(1)
        number_of_products_in_cart = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_CART).text
        print(number_of_products_in_cart)
        assert number_of_products_in_cart == 0 , "Error: The product was not removed from the cart"


    def test_login_invalid_email(self):
        self.chrome.find_element(*self.CONTUL_MEU).click()
        self.chrome.find_element(*self.INSERT_EMAIL).send_keys('test_selenium12345')
        self.chrome.find_element(*self.CONTINUA).click()

        # pui un mail fara @ si verifici mesajul de eroare


    def test_add_to_favourites(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT).click()
        self.chrome.find_element(*self.ADD_TO_FAV1).click()
        self.chrome.find_element(*self.OPEN_FAV).click()
        numbers_of_products_in_favorites = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_FAVORITES).text
        print(numbers_of_products_in_favorites)
        assert numbers_of_products_in_favorites == "1 produs", "Error: The product was removed from the favorites"

    def test_delete_from_favourites(self):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys(" Husa Iphone 14 Pro")
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.ADD_TO_FAV2_FROM_LIST).click()
        self.chrome.find_element(*self.OPEN_FAV).click()
        self.chrome.find_element(*self.DELETE_ELEMENT_FAV).click()
        sleep(1)
        numbers_of_products_in_favorites = self.chrome.find_element(*self.PRODUCT_COUNT_FROM_FAVORITES).text
        print(numbers_of_products_in_favorites)
        assert numbers_of_products_in_favorites == "0 produse", "Error: The product was not removed from the favorites"


# Sa inlocuiesti sleep-urile cu explicit wait


    # abonare la newsletter
    # - nume si email valid
    # - nume empty, mail valid
    # - nume empty, mail invalid
    # - nume valid, mail invalid

    # cautare produs husa iphone 15
    # filtrare dupa brand honor
    # sortare dupa pret crescator
    # salvare elemente in lista si verificare corectitudine sortare

    # salvezi xpath pret produs: self.chrome.find_element(By.XPATH,'//p[@class="product-new-price"]').text
    #  -> 7 81 Lei
    # -> aplici metoda replace pe textul care ti-a fost returnat pentru a extrage doar valoarea care te intereseaza
    # exemplu: inlocuiesti " Lei" cu "" apoi inlocuiesti " " cu "." -> 7.81
    # cu un for imbricat  parcurgi toate elementele
    # //div[@class="listing-sorting-dropdown"]
    # //div[@class="sort-control-btn-dropdown hidden-xs"]
    # este_lista_sortata = True
    # for i in range(len(pret_produse)-1):
    #     for j in range(i+1,len(pret_produse)):
    #         if pret_produse[i]>pret_produse[j]:
    #             este_lista_sortata = False
    # assert este_lista_sortata == True

    def test_choose_product_from_menu(self):
        self.chrome.find_element(*self.CAT_LAP_TEL_TAB).click()
        self.chrome.find_element(*self.TEL).click()
        self.chrome.find_element(*self.IOS).click()
        self.chrome.find_element(*self.LIVRATE_EMAG).click()
        self.chrome.find_element(*self.SECTOR).click()
        self.chrome.find_element(*self.IN_STOCK).click()
        self.chrome.find_element(*self.RANGE_PRET).click()
        self.chrome.find_element(*self.IPHONE_14).click()
        self.chrome.find_element(*self.CLICK_TELEFON).click()
        self.chrome.find_element(*self.ADD_TO_CART2).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        self.chrome.find_element(*self.DELETE_ELEMENT).click()
        self.chrome.find_element(*self.HOME).click()


    def test_resigilate(self):
        self.chrome.find_element(*self.RESIGILATE).click()
        self.chrome.find_element(*self.TELEFOANE_RESIGILATE).click()
        self.chrome.find_element(*self.TELEFON_SAMSUNG).click()
        self.chrome.find_element(*self.ADD_SAM_CART).click()
        sleep(1)
        self.chrome.find_element(*self.CLOSE_SUGGESTION).click()
        self.chrome.find_element(*self.CART).click()
        Element = self.chrome.find_element(By.XPATH, '//*[@class="line-item-title main-product-title"]')
        Element_cautat = 'RESIGILAT'
        if Element_cautat in Element.text:
            print('Telefonul este de la resigilate')
            self.chrome.find_element(*self.CONTINUE_FROM_CART).click()
            self.chrome.find_element(*self.INSERT_EMAIL).send_keys("test_selenium12345@gmail.com")
            self.chrome.find_element(*self.CONTINUA).click()
            self.chrome.back()
            self.chrome.find_element(*self.HOME).click()
        else:
            print('Telefonul nu este resigilat')
            self.chrome.find_element(*self.DELETE_ELEMENT).click()
            sleep(1)
            self.chrome.find_element(*self.GOTOMAG).click()



