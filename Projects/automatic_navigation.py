import unittest
from selenium import webdriver
from time import sleep

#IMPORTANTE#
# find_elements(find_element('id', 'firstname')) //instead// find_elements_by_id('select-language')

class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.get("https://www.google.com/")

	def test_browser_navigation(self):
		driver = self.driver

		search_field = driver.find_element('name', 'q')
		search_field.clear()
		search_field.send_keys('platzi')
		search_field.submit()

		driver.back()#retroceder navegador
		sleep(3) #espera 3 segundos
		driver.forward() #avanzar
		sleep(3) 
		driver.refresh() # actualizar página
		sleep(3)


	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)