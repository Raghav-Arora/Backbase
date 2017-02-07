import unittest
from pages import *
from testCases import *


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
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
        computerDetails = AddComputer(self.driver)
        self.assertTrue(computerDetails.check_page_loaded)
        computerDetails.get_status()
        computerDetails.add_details("Automated Test Computer", "2016-01-01", "2017-02-01", "Canon")
        assert page.success_message_is_displayed()

    def test_TC03_add_computer_via_direct_link(self):
        print "\n" + str(test_cases(2))
        page = HomePage(self.driver)
        page.open("/new")
        computerDetails = AddComputer(self.driver)
        self.assertTrue(computerDetails.check_page_loaded)
        computerDetails.add_details("Automated Test Computer via Direct Link", "2000-01-01", "2017-02-02", "Sony")
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
            computerDetails = AddComputer(self.driver)
            computerDetails.get_status()
            self.assertTrue(computerDetails.check_page_loaded)
            computerDetails.add_details(name, "2016-01-01", "2017-02-01", "Canon")
            self.assertTrue(page.get_status())
            #assert page.success_message_is_displayed()

    def test_TC05_filter_search(self):
        print "\n" + str(test_cases(4))
        page = HomePage(self.driver)
        search_text = page.search_computer("Automated")
        self.assertTrue(search_text in self.driver.page_source)

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
        computerDetails = AddComputer(self.driver)
        self.assertTrue(computerDetails.check_page_loaded)
        computerDetails.select_company("Apple Inc.")
        computerDetails.click_savebutton()
        page.get_status()
        assert page.success_message_is_displayed()

    def test_TC08_edit_computer_via_direct_link(self):
        print "\n" + str(test_cases(7))
        page = HomePage(self.driver)
        page.search_computer("Automated")
        value = page.get_computer_value()
        page.open("/" + value)
        computerDetails = AddComputer(self.driver)
        self.assertTrue(computerDetails.check_page_loaded)
        clear_date = computerDetails.find_element(*AddLocators.DISCONTINUED_TEXTFIELD)
        clear_date.clear()
        computerDetails.click_savebutton()
        page.get_status()
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
        computerDetails = AddComputer(self.driver)
        self.assertTrue(computerDetails.check_page_loaded)
        computerDetails.click_delete()
        page.get_status()
        assert page.success_message_is_displayed()

    def test_TC11_delete_computer_via_direct_link(self):
        print "\n" + str(test_cases(10))
        page = HomePage(self.driver)
        page.open("/1/delete")

        # Although it currently shows the Action not found screen
        # Thought it would be better to assert that the Computer Database text wasn't in the Source code

        self.assertFalse("Computers database" in self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
