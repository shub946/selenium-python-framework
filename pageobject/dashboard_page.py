from selenium import webdriver
from selenium.webdriver.common.by import By
class Dashboard:
    def __init__(self,driver):
        self.driver=driver
        self.welcome_msg="//h1[normalize-space()='Events']"
    def wel_text(self):
        return self.driver.find_element(By.XPATH, self.welcome_msg).text