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

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://phptravels.org/login')

    def tearDown(self) -> None:
        sleep(1000)
        self.chrome.quit()
