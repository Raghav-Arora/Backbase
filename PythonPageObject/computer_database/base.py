from selenium import webdriver
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This Base class is serving basic attributes for every single inherited from Page class

class Page(object):
    def __init__(self, driver, base_url="http://computer-database.herokuapp.com/computers"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_status(self):
        status = urllib.urlopen(self.base_url)
        return status.getcode()

