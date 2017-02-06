import unittest

from selenium import webdriver
from computer_database.pages import *
from testCases import *


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://computer-database.herokuapp.com/computers")

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())
        self.assertIn("Computers database", page.get_title())

    def test_add_computer(self):
        print "\n" + str(test_cases(1))
        page = HomePage(self.driver)
        page.click_add_computer()
        addcomputerpage = AddComputer(self.driver)
        addcomputerpage.check_page_loaded()
        print addcomputerpage.get_url()
        addcomputerpage.enter_computer_name("A1")




    def test_filter_search(self):
        print "\n" + str(test_cases(2))
        page = HomePage(self.driver)
        search_text = page.search_computer("A1")
        self.assertTrue(search_text in self.driver.page_source)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)