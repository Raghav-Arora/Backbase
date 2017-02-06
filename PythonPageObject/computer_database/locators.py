from selenium.webdriver.common.by import By

# Maintainability we can separate web objects by page name


class HomePageLocators(object):

    SEARCH_TEXTFIELD = (By.ID, 'searchbox')
    SEARCH_BUTTON = (By.ID, 'searchsubmit')
    ADD_BUTTON = (By.ID, 'add')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-message.warning')


class AddComputerLocators(object):

    COMPUTER_NAME_TEXTFIELD = (By.CSS_SELECTOR, '#name')
    INTRODUCED_TEXTFIELD = (By.ID, '.for introduced')
    DISCONTINUED_TEXTFIELD = (By.ID, 'discontinued')
    COMPANY_DROP_DOWN = (By.ID, 'company')
    CREATE_BUTTON = (By.ID, 'btn.primary')
    CANCEL_BUTTON = (By.LINK_TEXT, 'Cancel')


class EditComputerLocators(object):

    COMPUTER_NAME_TEXTFIELD = (By.ID, 'name')
    INTRODUCED_TEXTFIELD = (By.ID, 'introduced')
    DISCONTINUED_TEXTFIELD = (By.ID, 'discontinued')
    COMPANY_DROP_DOWN = (By.ID, 'company')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.btn.primary')
    CANCEL_BUTTON = (By.LINK_TEXT, 'Cancel')
    DELETE_BUTTON = (By.CSS_SELECTOR, '.btn.danger')