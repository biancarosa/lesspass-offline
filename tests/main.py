import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# LESSPASS_URL = "http://localhost:8000/#"
LESSPASS_URL = "https://lesspass-offline.biancarosa.com.br/#"

class LessPassHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        try:
            self.driver.get(LESSPASS_URL)
        except:
            self.fail("App is not up")

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
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', '/tmp')
        profile.set_preference(
            'browser.helperApps.neverAsk.saveToDisk', 'text/plain')
        self.driver = webdriver.Firefox(firefox_profile=profile)
        try:
            self.driver.get(LESSPASS_URL)
        except:
            self.fail("App is not up")

    def testCreatePasswordProfile(self):
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = self.driver.find_element_by_link_text(
            'Would you like to create one?')
        time.sleep(1)
        elem.click()
        elem = self.driver.find_element_by_id('siteField')
        elem.send_keys('Site')
        elem = self.driver.find_element_by_id('login')
        elem.send_keys('Login')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('generatePassword__btn')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_id('revealGeneratedPassword')
        elem.click()
        elem = self.driver.find_element_by_id('generated-password')
        self.assertEqual(elem.get_attribute('value'), '="9MLMjZ6yf&FTi{')
        elem = self.driver.find_element_by_xpath(
            "//span[@title='Save']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = self.driver.find_element_by_xpath(
            "//div[@class='passwordProfile']/div/div[@class='passwordProfile__meta']")
        self.assertEqual(elem.text, 'Site\nLogin')
        elem.click()
        time.sleep(3)
        elem = self.driver.find_element_by_id('title')
        self.assertEqual(elem.text, 'LessPass')
        elem.click()
        time.sleep(3)
        elem = self.driver.find_element_by_id('siteField')
        elem.send_keys('Site2')
        elem = self.driver.find_element_by_id('login')
        elem.send_keys('Login2')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('generatePassword__btn')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//span[@title='Save']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elems = self.driver.find_elements_by_xpath(
            "//div[@class='passwordProfile']/div/div[@class='passwordProfile__meta']")
        self.assertEqual(elems[0].text, 'Site\nLogin')
        self.assertEqual(elems[1].text, 'Site2\nLogin2')
        elem.click()
        time.sleep(3)

    def testExportPasswordProfile(self):
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = self.driver.find_element_by_link_text(
            'Would you like to create one?')
        time.sleep(1)
        elem.click()
        elem = self.driver.find_element_by_id('siteField')
        elem.send_keys('Site')
        elem = self.driver.find_element_by_id('login')
        elem.send_keys('Login')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('generatePassword__btn')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_id('revealGeneratedPassword')
        elem.click()
        elem = self.driver.find_element_by_id('generated-password')
        self.assertEqual(elem.get_attribute('value'), '="9MLMjZ6yf&FTi{')
        elem = self.driver.find_element_by_xpath(
            "//span[@title='Save']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = selem = self.driver.find_element_by_xpath(
            "//div[@class='passwordProfile']/div/div[@class='passwordProfile__meta']")
        self.assertEqual(elem.text, 'Site\nLogin')
        elem.click()
        time.sleep(3)

        elem = self.driver.find_element_by_xpath(
            "//a[@title='Export Password Profiles']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_id('email')
        elem.send_keys('email@email.com.br')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('btn-submit-settings')
        elem.click()
        time.sleep(3)
        with open('/tmp/profiles.lp', 'r') as f:
            self.assertEqual(' {"profiles":"9a1576473ce593557f5b7a05e038ae410d0fc062fee0e2d2543e3f1585db3ae3d9da118d1ca754fd00c5f76fcfca43f470f10f64c03b2131a6101e4b7a28d77e0d1fe6a89f05ee94a8b895608b465f53a59fac19a8c974a43d3e616ffdaf7aa72b7aa3d5be766c918267c5a26da5bbf494a1b9f2f3672e6230fb474c506b01f6b025e583e8ba4600808a711c08c988cd","key":"a556543b47d3d3613ed53e53134ce660323d40bfc93cd7c0596fec814c3c0499"}', f.read())
        os.remove('/tmp/profiles.lp')

    def testImportPasswordProfiles(self):
        with open('/tmp/profiles.lp', 'w') as f:
            f.write(' {"profiles":"9a1576473ce593557f5b7a05e038ae410d0fc062fee0e2d2543e3f1585db3ae3d9da118d1ca754fd00c5f76fcfca43f470f10f64c03b2131a6101e4b7a28d77e0d1fe6a89f05ee94a8b895608b465f53a59fac19a8c974a43d3e616ffdaf7aa72b7aa3d5be766c918267c5a26da5bbf494a1b9f2f3672e6230fb474c506b01f6b025e583e8ba4600808a711c08c988cd","key":"a556543b47d3d3613ed53e53134ce660323d40bfc93cd7c0596fec814c3c0499"}')
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Import Password Profiles']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_id('email')
        elem.send_keys('email@email.com.br')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('profiles')
        elem.send_keys('/tmp/profiles.lp')
        elem = self.driver.find_element_by_id('btn-submit-settings')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = selem = self.driver.find_element_by_xpath(
            "//div[@class='passwordProfile']/div/div[@class='passwordProfile__meta']")
        self.assertEqual(elem.text, 'Site\nLogin')
        elem.click()
        time.sleep(3)
    
    def testAddNewPasswordToImportedPasswordProfiles(self):
        with open('/tmp/profiles.lp', 'w') as f:
            f.write(' {"profiles":"9a1576473ce593557f5b7a05e038ae410d0fc062fee0e2d2543e3f1585db3ae3d9da118d1ca754fd00c5f76fcfca43f470f10f64c03b2131a6101e4b7a28d77e0d1fe6a89f05ee94a8b895608b465f53a59fac19a8c974a43d3e616ffdaf7aa72b7aa3d5be766c918267c5a26da5bbf494a1b9f2f3672e6230fb474c506b01f6b025e583e8ba4600808a711c08c988cd","key":"a556543b47d3d3613ed53e53134ce660323d40bfc93cd7c0596fec814c3c0499"}')
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Import Password Profiles']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_id('email')
        elem.send_keys('email@email.com.br')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('profiles')
        elem.send_keys('/tmp/profiles.lp')
        elem = self.driver.find_element_by_id('btn-submit-settings')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elem = selem = self.driver.find_element_by_xpath(
            "//div[@class='passwordProfile']/div/div[@class='passwordProfile__meta']")
        self.assertEqual(elem.text, 'Site\nLogin')
        elem.click()
        time.sleep(3)
        elem = self.driver.find_element_by_id('title')
        self.assertEqual(elem.text, 'LessPass')
        elem.click()
        time.sleep(3)
        elem = self.driver.find_element_by_id('siteField')
        elem.send_keys('Site2')
        elem = self.driver.find_element_by_id('login')
        elem.send_keys('Login2')
        elem = self.driver.find_element_by_id('passwordField')
        elem.send_keys('123123')
        elem = self.driver.find_element_by_id('generatePassword__btn')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//span[@title='Save']")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "//a[@title='Saved passwords']")
        elem.click()
        elems = self.driver.find_elements_by_xpath(
            "//div[@class='passwordProfile']/div/div[@class='passwordProfile__meta']")
        self.assertEqual(elems[0].text, 'Site\nLogin')
        self.assertEqual(elems[1].text, 'Site2\nLogin2')
        elem.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

