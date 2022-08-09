from encodings import search_function
from itertools import product
from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver

class Searchstests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.impricity_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        self.driver = self.driver
        search_field= driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        self.assertEqual(), len(products)


    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)