import pytest
from selene.support import webdriver
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='function')
def headless_chrome():
    options = webdriver.ChromeOptions()
    options=Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')



def test_browser_search(headless_chrome):
    browser.config.timeout = 10
    browser.open("https://demoqa.com/automation-practice-form")


