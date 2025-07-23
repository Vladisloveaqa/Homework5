import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def headless_chrome():
    options = Options()

    options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    yield
    driver.quit()