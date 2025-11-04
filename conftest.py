import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.urls import Urls

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(Urls.XYZ_BANK_URL)
    yield driver
    driver.quit()