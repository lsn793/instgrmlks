from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, driver, base_url='http://www.app.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
 
    def find_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator))
            )
            return element
        except:
            return False

    def find_all_elements(self, *locator):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((locator))
            )
            return elements
        except:
            return False

    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()    
