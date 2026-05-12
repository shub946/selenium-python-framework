import time

from selenium import webdriver
import pytest
#ye utility file yaha configure karne k liye kiya he
driver=None
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")
@pytest.fixture()
def setup(request):
    request.cls.driver=webdriver.Chrome()
    request.cls.driver.get(config.get("url","base_url"))
    time.sleep(20)
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.quit()


