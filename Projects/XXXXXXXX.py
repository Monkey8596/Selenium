import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 

class HelloWorld(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.aupairworld.com/es')

    def familia_encontrar(self):
        search_field = self.driver.find_element_by_id('//*[@id="block-aupairworld-entityviewcontent"]/article/div/div/div/div[2]/div/div/div/a[1]')
        search_field.click()

    def familia_encontrar(self):
        search_field = self.driver.find_element_by_id(' /html/body')
        search_field.click()


    #@classmethod
    # def tearDownClass(cls):
    #    cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))