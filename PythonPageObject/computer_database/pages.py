from computer_database.base import Page
from selenium.webdriver.common.keys import Keys
from locators import *


class HomePage(Page):

    def check_page_loaded(self):
        return True if self.get_status() == 200 else False

    def search_computer(self, item):
        self.find_element(*HomePageLocators.SEARCH_TEXTFIELD).send_keys(item)
        self.find_element(*HomePageLocators.SEARCH_BUTTON).click()

    def click_add_computer(self):
        self.driver.find_element(*HomePageLocators.ADD_BUTTON).click()
        return AddComputer(self.driver)


class AddComputer(Page):
    def check_page_loaded(self):
        return True if self.get_status() == 200 else False

    def enter_computer_name(self, data):
        self.driver.find_element(*AddComputerLocators.COMPUTER_NAME_TEXTFIELD).send_keys(data.get_data(data)["name"])

    def enter_intro_data(self, data):
        self.driver.find_element(*AddComputerLocators.INTRODUCED_TEXTFIELD).send_keys(data.get_data(data)["intro_date"])

    def enter_discontinued(self, data):
        self.driver.find_element(*AddComputerLocators.DISCONTINUED_TEXTFIELD).send_keys(data.get_data(data)["discontinued"])

    def click_addbutton(self):
        self.driver.find_element(*AddComputerLocators.CREATE_BUTTON).click()

        # return HomePage(self.driver)


