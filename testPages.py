import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages import *
from testCases import test_cases
from users import site
from locators import *


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestPages(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("user-data-dir=" + site["userprofile"])
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver = webdriver.Firefox()
        self.driver.get(site["url"])

    #def test_page_load(self):
    #    print ("\n" + str(test_cases(0)))
    #    page = LoginPage(self.driver)
    #    somePage = page.log_in("serj") #somePage maybe popup page with mobile advertizing
    #    if not somePage.close_popup_page():
    #        self.fail("Could not close popup page")
    #    userPage = somePage.goto_homepage()
    #    print(userPage.get_num_posts())
    #    print(userPage.get_num_followers())
    #    print(userPage.get_num_following())

    def test_search_item(self):
        print ("\n" + str(test_cases(1)))
        page = SomePage(self.driver)
        homePage = page.goto_homepage()
        print(homePage.get_num_posts())
        print(homePage.get_num_followers())
        print(homePage.get_num_following())

        searchPage = homePage.search_by_hashtag("#дети")
        searchPage.enum_posts();

    #def test_sign_up_button(self):
    #    print "\n" + str(test_cases(2))
    #    page = MainPage(self.driver)
    #    signUpPage = page.click_sign_up_button()
    #    self.assertIn("ap/register", signUpPage.get_url())

    #def test_sign_in_button(self):
    #    print "\n" + str(test_cases(3))
    #    page = MainPage(self.driver)
    #    loginPage = page.click_sign_in_button()
    #    self.assertIn("ap/signin", loginPage.get_url())

    #def test_sign_in_with_valid_user(self):
    #    print "\n" + str(test_cases(4))
    #    mainPage = MainPage(self.driver)
    #    loginPage = mainPage.click_sign_in_button()
    #    result = loginPage.login_with_valid_user("valid_user")
    #    self.assertIn("yourstore/home", result.get_url())

    #def test_sign_in_with_in_valid_user(self):
    #    print "\n" + str(test_cases(5))
    #    mainPage = MainPage(self.driver)
    #    loginPage = mainPage.click_sign_in_button()
    #    result = loginPage.login_with_in_valid_user("invalid_user")
    #    self.assertIn("There was a problem with your request", result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

