import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome() #open browser
    driver.maximize_window()    #open full screen
    driver.implicitly_wait(10)  #whait 10 sec if not found elements
    yield driver