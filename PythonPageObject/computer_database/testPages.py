import unittest
from pages import *
from testCases import *
from selenium import webdriver

# This page is where the Test Cases are defined that match against the Automated Tests marked Y in the Test Script
# Note that other web drivers are potentially available such as webdriver.Chrome(), webdriver.IE, webdriver.Safari()


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://computer-database.herokuapp.com/computers")

    def test_TC01_page_load(self):
        print "\n" + str(test_cases(0))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())
        self.assertIn("Computers database", page.get_title())

    def test_TC02_add_computer(self):
        print "\n" + str(test_cases(1))
        page = HomePage(self.driver)
        page.click_add_computer()
        computer_details = AddComputer(self.driver)
        self.assertTrue(computer_details.check_page_loaded)
        computer_details.add_details("Automated Test Computer", "2016-01-01", "2017-02-01", "Canon")
        assert page.success_message_is_displayed()

    def test_TC03_add_computer_via_direct_link(self):
        print "\n" + str(test_cases(2))
        page = HomePage(self.driver)
        page.open("/new")
        computer_details = AddComputer(self.driver)
        self.assertTrue(computer_details.check_page_loaded)
        computer_details.add_details("Automated Test Computer via Direct Link", "2000-01-01", "2017-02-02", "Sony")
        assert page.success_message_is_displayed()

    def test_TC04_invalid_inputs_add_computer(self):
        print "\n" + str(test_cases(3))
        page = HomePage(self.driver)

        invalid = ["<html><a>\"dsad\"</a></html>","A'", "~!@#$%^&*()_+{}|:<>?`-',./", " Lorem ipsum dolor sit amet, \
        consectetur adipiscing elit. Maecenas ac consequat dui. Quisque erat turpis, rhoncus ut imperdiet euismod, \
        iaculis a quam. Quisque malesuada, velit quis viverra gravida, nunc leo tempor arcu, vitae pulvinar sapien dui \
        ut neque. Suspendisse potenti. Vestibulum arcu mauris, varius et egestas ut, fringilla quis lorem. Integer \
        ullamcorper gravida varius."]

        for name in invalid:
            page.get_status()
            page.check_page_loaded()
            page.click_add_computer()
            computer_details = AddComputer(self.driver)
            self.assertTrue(computer_details.check_page_loaded)
            computer_details.add_details(name, "2016-01-01", "2017-02-01", "Canon")
            assert page.success_message_is_displayed()

    def test_TC05_filter_search(self):
        print "\n" + str(test_cases(4))
        page = HomePage(self.driver)
        page.search_computer("Automated")
        page.get_status()
        search_result = page.get_search_result()
        self.assertTrue(search_result in self.driver.page_source)

    def test_TC06_filter_search_via_direct_link(self):
        print "\n" + str(test_cases(5))
        page = HomePage(self.driver)
        page.open("?f=Automated+Test")
        self.assertIn("?f=Automated+Test", page.get_url())

    def test_TC07_edit_computer(self):
        print "\n" + str(test_cases(6))
        page = HomePage(self.driver)
        page.search_computer("Automated")
        page.click_link("Automated Test Computer")
        computer_details = AddComputer(self.driver)
        self.assertTrue(computer_details.check_page_loaded)
        computer_details.select_company("Apple Inc.")
        computer_details.click_savebutton()
        assert page.success_message_is_displayed()

    def test_TC08_edit_computer_via_direct_link(self):
        print "\n" + str(test_cases(7))
        page = HomePage(self.driver)
        page.search_computer("Automated")
        value = page.get_computer_value()
        page.open("/" + value)
        computer_details = AddComputer(self.driver)
        self.assertTrue(computer_details.check_page_loaded)
        clear_date = computer_details.find_element(*AddLocators.DISCONTINUED_TEXTFIELD)
        clear_date.clear()
        computer_details.click_savebutton()
        assert page.success_message_is_displayed()

    def test_TC09_edit_computer_via_direct_link_non_existent(self):
        print "\n" + str(test_cases(8))
        page = HomePage(self.driver)
        page.open("/12154")
        self.assertFalse("Computers database" in self.driver.page_source)

    def test_TC10_delete_computer(self):
        print "\n" + str(test_cases(9))
        page = HomePage(self.driver)
        page.search_computer("Automated")
        page.click_link("Automated Test Computer")
        computer_details = AddComputer(self.driver)
        self.assertTrue(computer_details.check_page_loaded)
        computer_details.click_delete()
        assert page.success_message_is_displayed()

    def test_TC11_delete_computer_via_direct_link(self):
        print "\n" + str(test_cases(10))
        page = HomePage(self.driver)
        page.open("/1/delete")

        # Although it currently shows the Action not found screen
        # Thought it would be better to assert that the Computer Database text wasn't in the Source code

        self.assertFalse("Computers database" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
