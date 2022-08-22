import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class MercadoLibre(unittest.TestCase):
    

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.get('https://mercadolibre.com')
        
    def test_search_ps4(self):
        driver = self.driver
        country = driver.find_element('id', 'CO')
        country.click()
        sleep(3)

        cookies_in = driver.find_element('xpath',"/html/body/div[2]/div[1]/div[2]/button[1]") 
        cookies_in.click()
        sleep(3)

        search_field = driver.find_element('name','as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)


        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element(By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element('xpath', f'/html/body/main/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element('xpath', f'/html/body/main/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles,prices)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)