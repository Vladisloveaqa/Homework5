from selene.support.shared import browser
from selene import be, have

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
    dob_input =browser.element('#dateOfBirthInput')
    dob_input.click()
    dob_input.clear()
    dob_input.type('02 Jun 1999').press_enter()









