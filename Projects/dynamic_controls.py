import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

#IMPORTANTE#
# find_elements(find_element('id', 'firstname')) //instead// find_elements_by_id('select-language')


from selenium.webdriver.chrome import options

class Dynamic_controls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Dynamic Controls").click()

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()

        remove_add_buttom = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_buttom.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_buttom.click()

        enable_desable_buttom = driver.find_element_by_css_selector("#input-example > button")
        enable_desable_buttom.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#input-example > button")))
        
        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.send_keys('Platzi')

        enable_desable_buttom.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output="reportes", report_name="prueba_asssert"))