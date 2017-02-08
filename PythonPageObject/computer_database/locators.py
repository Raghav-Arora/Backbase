from selenium.webdriver.common.by import By

# Maintainability we can separate web objects by page name
# Locators for each page are defined here.


class HomePageLocators(object):

    SEARCH_TEXTFIELD = (By.ID, 'searchbox')
    SEARCH_BUTTON = (By.ID, 'searchsubmit')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'table td > a')
    ADD_BUTTON = (By.ID, 'add')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-message')


class AddLocators(object):

    NAME_TEXTFIELD = (By.ID, 'name')
    INTRO_TEXTFIELD = (By.ID, 'introduced')
    DISCONTINUED_TEXTFIELD = (By.ID, 'discontinued')
    COMPANY_DROP_DOWN = (By.ID, 'company')
    CREATE_BTN = (By.CSS_SELECTOR, '.primary')
    CANCEL_BTN = (By.LINK_TEXT, 'Cancel')


class EditLocators(object):

    DELETE_BUTTON = (By.CSS_SELECTOR, '.btn.danger')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.primary')