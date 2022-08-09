import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.impricity_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    
    def is_element_present(self, how, what ):
        try:
            self.driver.find_element(by = how, value= what)
        except NoSuchAttributeException as variable:
            return False
        return True


    def tes_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))


    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)