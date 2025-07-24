from selene.support.shared import browser
from selene import be, have
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


#тест проверяет наличие нужного заголовка на странице
def test_browser_search(headless_chrome):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('h5').should(have.exact_text('Student Registration Form'))
    browser.element('h5').should(be.visible)

def test_vvod_formi(headless_chrome):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').should(be.blank).type('Vladislav')
    browser.element('#firstName').should(have.value('Vladislav'))
    browser.element('#lastName').should(be.blank).type('Wqw')
    browser.element('#lastName').should(have.value('Wqw'))
    browser.element('#userEmail').should(be.blank).type('mr.vlad0007@gmail.com')
    browser.element('#userEmail').should(have.value('mr.vlad0007@gmail.com'))
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#gender-radio-1').should(be.selected)
    browser.element('#userNumber').should(be.blank).type('9992103884')
    browser.element('#userNumber').should(have.value('9992103884'))
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="5"]').click()  # June (нумерация с 0)
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1999"]').click()
    browser.element('.react-datepicker__day--002:not(.react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('.subjects-auto-complete__multi-value__label').should(have.text('Maths'))
    browser.element('[for="hobbies-checkbox-3"]').should(be.visible).click()
    browser.element('#hobbies-checkbox-3').should(be.selected)
    browser.element('#uploadPicture').send_keys('C:\\Users\\KagePC\\Desktop\\фотка.jpg')
    browser.element('#currentAddress').should(be.blank).type('Санкт-Петербург , пр-т Большевиков , корпус 14')
    browser.element('#currentAddress').should(have.value('Санкт-Петербург , пр-т Большевиков , корпус 14'))
    browser.element('#state').click()
    browser.element('//div[text()="Haryana"]').click()
    browser.element('#city').click()
    browser.element('//div[text()="Karnal"]').click()
    browser.element('#submit').click()
    browser.all('.table-responsive td').should(have.exact_texts(
    'Student Name', 'Vladislav Wqw',
    'Student Email', 'mr.vlad0007@gmail.com',
    'Gender', 'Male',
    'Mobile', '9992103884',
    'Date of Birth', '02 June,1999',
    'Subjects', 'Maths',
    'Hobbies', 'Music',
    'Picture', 'фотка.jpg',
    'Address', 'Санкт-Петербург , пр-т Большевиков , корпус 14',
    'State and City', 'Haryana Karnal'
    ))












