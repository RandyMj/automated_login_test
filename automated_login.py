import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class logTest(unittest.TestCase):

    def setUp(self):
        PATH = "C:\Selenium_Drivers\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_logIn(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(1.5)

        user = driver.find_element_by_id("user-name")
        user.clear()
        user.send_keys("standard_user")
        time.sleep(1.5)

        password = driver.find_element_by_id("password")
        password.clear()
        password.send_keys("secret_sauce")
        time.sleep(1.5)

        button = driver.find_element_by_id("login-button")
        button.click()
        time.sleep(1.5)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
