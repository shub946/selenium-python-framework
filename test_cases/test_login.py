import time



from selenium import webdriver
import pytest

from selenium.webdriver.common.by import By
from pageobject.login_page import Login
from pageobject.dashboard_page import Dashboard
#for logs implement
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup")
class Test_Login_page(logclass):
    def test_login01(self):
        lg=Login(self.driver)
        #this will know always
        logger = self.getthelogs()
        logger.info("Test CASE 001")
        logger.info("test starting")
        lg.input_name(config.get("credential","correct_username"))
        logger.info("entered username")
        lg.input_pass(config.get("credential","incorrect_password"))
        logger.info("entered Password")
        lg.click()
        logger.info("Click the login button")
        time.sleep(10)
        if 'msg' in lg.invalid_cred():
            assert True
            logger.info("testcase pass")
        else:
            False
            logger.critical("test fail")
    def test_login02(self):
        lg=Login(self.driver)
        lg.input_name(config.get("credential", "correct_username"))
        lg.input_pass(config.get("credential", "blank_password"))
        lg.click()
        time.sleep(10)
        if 'BP' in lg.nopassword():
            assert True
        else:
            False
    def test_login03(self):
        lg=Login(self.driver)
        lg.input_name("")
        lg.input_pass("Password1")
        lg.click()
        time.sleep(10)
        if 'BP' in lg.nousername():
            assert True
        else:
            False
    def test_login04(self):
        lg=Login(self.driver)
        lg.input_name("")
        lg.input_pass("")
        lg.click()
        time.sleep(10)
        if 'BUP' in lg.Blak_Both():
            assert True
        else:
            False

    def test_login05(self):
            lg = Login(self.driver)
            DB = Dashboard(self.driver)
            lg.input_name("qauser001")
            lg.input_pass("Password1")
            lg.click()
            time.sleep(10)
            if 'welcome' in DB.wel_text():
                assert True
            else:
                False

        #driver = webdriver.Chrome()
        #driver.get("https://wccqa.on24.com/webcast/login")
        #time.sleep(10)
        #self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("qauser001")
        #self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password1")
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #time.sleep(30)
        #self.driver.save_screenshot("screenshot1.png")
        #if 'Event' in self.driver.find_element(By.XPATH, "//h1[normalize-space()='Events']").text:
           # assert True
        #else:
            #assert False