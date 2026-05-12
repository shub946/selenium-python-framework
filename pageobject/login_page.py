import time

from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver=driver
        self.username="//input[@id='username']"
        self.password="//input[@name='password']"
        self.login="//button[@type='submit']"
        self.invalid_message="//div[@class='MuiAlert-message css-127h8j3']"
        self.Blank_username= "//span[@class='css-1rjegds']"
        self.Blank_password = "//span[@id='password-error']"
        self.Blank_username_password="//span[@id='username-error']"
        time.sleep(20)
    def input_name(self, username):
        self.driver.find_element(By.XPATH, self.username).send_keys(username)
        time.sleep(20)
    def input_pass(self,password):
        self.driver.find_element(By.XPATH, self.password).send_keys(password)
    def click(self):
        self.driver.find_element(By.XPATH, self.login).click()
    def invalid_cred(self):
        return self.driver.find_element(By.XPATH, self.invalid_message).text
    def nopassword(self):
        return self.driver.find_element(By.XPATH, self.Blank_password).text
    def nousername(self):
        return self.driver.find_element(By.XPATH, self.Blank_username).text
    def Blak_Both(self):
        return self.driver.find_element(By.XPATH, self.Blank_username_password).text
