import pytest
from seleniumwire import webdriver

from pageobject.dashboard_page import Dashboard
from pageobject.login_page import Login
import configparser
configparaser=configparser.configParaser()
@pytest.fixture()
def setup(request):
    request.cls.driver=webdriver.Chrome()
    request.cls.driver.get("")
    request.cls.driver.window_maximize()
    yield
    request.cls.driver.quit()

#fisrt create conftest.py file in test package
@pytest.mark.usefixtures(setup)
class Test_loginpage():
    def test_one(self):
        lg= Login(self.driver)
        Db= Dashboard(self.driver)
        lg.input_username()
        lg.input_pass()
        lg.click()
        if 'welcome' in Db.wel_text():
            assert True
        else:
                False