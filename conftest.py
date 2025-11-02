import pytest
from data.urls import Urls
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.XYZ_BANK_URL)
    yield driver
    driver.quit()