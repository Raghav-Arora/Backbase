from base import Page
from selenium.webdriver.support.ui import Select
from locators import *



class HomePage(Page):

    def check_page_loaded(self):
        return True if self.get_status() == 200 else False

    def search_computer(self, item):
        self.find_element(*HomePageLocators.SEARCH_TEXTFIELD).send_keys(item)
        self.find_element(*HomePageLocators.SEARCH_BUTTON).click()
        return item

    def success_message_is_displayed(self):
        successElement = self.driver.find_element(*HomePageLocators.SUCCESS_MESSAGE)
        return successElement.is_displayed()

    def click_add_computer(self):
        self.driver.find_element(*HomePageLocators.ADD_BUTTON).click()

    def click_link(self,search_text):
        self.driver.find_element_by_link_text(search_text).click()

    def get_computer_value(self):
        self.get_status()
        url = self.driver.find_element(*HomePageLocators.SEARCH_RESULT)
        url = url.get_attribute('href').split('/')[-1]
        return url

    def get_search_result(self):
        url = self.driver.find_element(*HomePageLocators.SEARCH_RESULT)
        url = url.get_attribute('text')
        return url


class AddComputer(Page):
    def check_page_loaded(self):
        return True if self.get_status() == 200 else False

    def check_page_failure(self):
        return True if self.get_status() == 404 else False

    def click_delete(self):
        deleteBtn = self.driver.find_element(*EditLocators.DELETE_BUTTON)
        deleteBtn.click()

    def enter_computer_name(self, NAME_TEXTFIELD):
        nameElement = self.driver.find_element(*AddLocators.NAME_TEXTFIELD)
        nameElement.send_keys(NAME_TEXTFIELD)

    def enter_intro_date(self, INTRO_TEXTFIELD):
        introElement = self.driver.find_element(*AddLocators.INTRO_TEXTFIELD)
        introElement.send_keys(INTRO_TEXTFIELD)

    def enter_discontinued(self, DISCONTINUED_TEXTFIELD):
        EndDate = self.driver.find_element(*AddLocators.DISCONTINUED_TEXTFIELD)
        EndDate.send_keys(DISCONTINUED_TEXTFIELD)

    def select_company(self, value):
        CompanyName = Select(self.driver.find_element(*AddLocators.COMPANY_DROP_DOWN))
        CompanyName.select_by_visible_text(value)

    def click_addbutton(self):
        submitBtn = self.driver.find_element(*AddLocators.CREATE_BTN)
        submitBtn.click()

    def click_savebutton(self):
        saveBtn = self.driver.find_element(*EditLocators.SAVE_BUTTON)
        saveBtn.click()

    def add_details(self, NAME_TEXTFIELD, INTRO_TEXTFIELD, DISCONTINUED_TEXTFIELD,value):
        self.enter_computer_name(NAME_TEXTFIELD)
        self.enter_intro_date(INTRO_TEXTFIELD)
        self.enter_discontinued(DISCONTINUED_TEXTFIELD)
        self.select_company(value)
        self.click_addbutton()
