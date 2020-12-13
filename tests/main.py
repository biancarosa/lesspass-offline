import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LESSPASS_URL = "http://localhost:8000/#"


class LessPassHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(LESSPASS_URL)

    def testImportPasswordProfilesExistOnHomePage(self):
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Import Password Profiles']")
        href = elem.get_attribute("href")
        self.assertEqual(href, f"{LESSPASS_URL}/profiles/import")

    def testSavedPasswordButtonExistsOnHomePage(self):
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        href = elem.get_attribute("href")
        self.assertEqual(href, f"{LESSPASS_URL}/passwords")

    def tearDown(self):
        self.driver.close()

class LessPassPasswordPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(LESSPASS_URL)

    def testCreatePasswordProfile(self):
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = self.driver.find_element_by_link_text(
            'Would you like to create one?')
        elem.click()
        elem = self.driver.find_element_by_id('siteField')
        elem.send_keys('Site')
        elem = self.driver.find_element_by_id('login')
        elem.send_keys('Login')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('generatePassword__btn')
        elem.click()
        elem = self.driver.find_element_by_id('revealGeneratedPassword')
        elem.click()
        elem = self.driver.find_element_by_id('generated-password')
        self.assertEqual(elem.get_attribute('value'), '="9MLMjZ6yf&FTi{')
        elem = self.driver.find_element_by_xpath(
            "//span[@title='Save']")
        elem.click()
        self.assertEqual(self.driver.current_url, f"{LESSPASS_URL}/passwords")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

