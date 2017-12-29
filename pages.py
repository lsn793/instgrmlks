from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
import users
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from random import uniform
from helper import more_than_two


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class LoginPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocatars.LOGO) else False

    def search_item(self, item):
        self.find_element(*MainPageLocatars.SEARCH).send_keys(item)
        self.find_element(*MainPageLocatars.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*MainPageLocatars.SEARCH_LIST).text
        
    def click_sign_up_button(self):
        self.hover(*MainPageLocatars.ACCOUNT)
        self.find_element(*MainPageLocatars.SIGNUP).click()
        return SignUpPage(self.driver)

    def click_sign_in_button(self):
        self.hover(*MainPageLocatars.ACCOUNT)
        self.find_element(*MainPageLocatars.LOGIN).click()
        return LoginPage(self.driver)
    
    def log_in(self, user):
        self.find_element(*LoginPageLocatars.LOGIN_LINK).click()
        self.find_element(*LoginPageLocatars.USERNAME).send_keys(users.get_user(user)["username"])
        self.find_element(*LoginPageLocatars.PASSWORD).send_keys(users.get_user(user)["password"])
        sleep(uniform(2, 3))
        self.find_element(*LoginPageLocatars.LOGIN_BUTTON).click()
        return SomePage(self.driver)


class MainPage(Page):
    def enter_email(self, user):
        self.find_element(*LoginPageLocatars.EMAIL).send_keys(users.get_user(user)["email"])

    def enter_password(self, user):
        self.find_element(*LoginPageLocatars.PASSWORD).send_keys(users.get_user(user)["password"])

    def click_login_button(self):
        self.find_element(*LoginPageLocatars.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocatars.ERROR_MESSAGE).text    
    
class CommonPage(Page):
    def goto_homepage(self):
        sleep(uniform(2, 4))
        self.find_element(*CommonPageLocatars.HOMEPAGE).click()
        return HomePage(self.driver)

    def get_num_posts(self):
        str = self.find_element(*CommonPageLocatars.NUM_POSTS).text
        pos = str.find(' ')
        num = str[:pos]
        return num

    def get_num_followers(self):
        str = self.find_element(*CommonPageLocatars.NUM_FOLLOWERS).text
        pos = str.find(' ')
        num = str[:pos]
        return num

    def get_num_following(self):
        str = self.find_element(*CommonPageLocatars.NUM_FOLLOWING).text
        pos = str.find(' ')
        num = str[:pos]
        return num    

    def search_by_hashtag(self, hashtag):
        self.find_element(*CommonPageLocatars.SEARCH).click()
        self.find_element(*CommonPageLocatars.SEARCH_BAR).send_keys(hashtag)
        sleep(uniform(2, 4))
        self.find_element(*CommonPageLocatars.SEARCH_BAR).send_keys(Keys.ENTER)
        sleep(uniform(1, 2))
        self.find_element(*CommonPageLocatars.SEARCH_BAR).send_keys(Keys.ENTER)
        return SearchPage(self.driver)


class SomePage(CommonPage):
    def close_popup_page(self): 
        #has url  url:https://www.instagram.com/#reactivated
        sleep(uniform(2, 3))
        element = self.find_element(*PopupPageLocatars.NOTNOW)
        if element:
            element.click()
            return True

        element = self.find_element(*PopupPageLocatars.CLOSE)
        if element:
            element.click()
            return True
        
        return False

class HomePage(CommonPage):
    pass

class UserPage(CommonPage):
    pass

class SearchPage(CommonPage):
    def get_num_views(self):
        try:
            el = find_element(*SearchPageLocatars.NUM_VIEWS)
            str = el.text
            print (str)
            pos = str.find('views')
            num = str[:pos]
            return num
        except:
            return False 

    def get_num_likes(self):
        try:
            el = find_element(*SearchPageLocatars.NUM_LIKES)
            str = el.text
            print (str)
            pos = str.find('likes')
            num = str[:pos]
            return num
        except:
            return False

    def get_num_comments(self):
        try:
            el = find_element(*SearchPageLocatars.NUM_COMMENTS)
            str = el.text
            print (str)
            pos = str.find('comments')
            num = str[:pos]
            return num 
        except:
            return False   

    def get_num_posts(self):
        num = self.find_element(*SearchPageLocatars.NUM_POSTS).text
        return num

    def enum_posts(self):
        elements = WebDriverWait(self.driver, 10).until(more_than_two((*SearchPageLocatars.POST_MOST_RECENT)))
        for el in elements:
            self.hover_element(el)
            sleep(uniform(5, 7))
            #num_views = self.get_num_views()
            #if (num_views):
            #    print (num_views)
            #else:
            #    print (self.get_num_likes())
            print (self.get_num_comments())
            
        print (len(elements))
        sleep(uniform(5, 7))

        