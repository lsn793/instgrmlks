from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
  LOGO          = (By.ID, 'nav-logo')
  ACCOUNT       = (By.ID, 'nav-link-yourAccount')
  SIGNUP        = (By.CSS_SELECTOR, '#nav-flyout-ya-newCust > a')
  LOGIN         = (By.CSS_SELECTOR, '#nav-flyout-ya-signin > a')
  SEARCH        = (By.ID, 'twotabsearchtextbox')
  SEARCH_LIST   = (By.ID, 's-results-list-atf')

class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'ap_email')
  PASSWORD      = (By.ID, 'ap_password')
  SUBMIT        = (By.ID, 'signInSubmit-input')
  ERROR_MESSAGE = (By.ID, 'message_error')
  LOGIN_LINK    = (By.LINK_TEXT, 'Log in')
  USERNAME      = (By.NAME, 'username')
  PASSWORD      = (By.NAME, 'password')
  LOGIN_BUTTON  = (By.TAG_NAME, 'button')

class PopupPageLocatars(object):
  CLOSE         = (By.XPATH, '//button[text()="Close"]')
  NOTNOW        = (By.LINK_TEXT, 'Not Now')

class CommonPageLocatars(object):
  HOMEPAGE      = (By.LINK_TEXT, 'Profile')
  NUM_POSTS     = (By.XPATH, '//header//li//span[text()=" posts"]')
  NUM_FOLLOWERS = (By.XPATH, '//header//li//span[text()=" followers"]')
  NUM_FOLLOWING = (By.XPATH, '//header//li//span[text()=" following"]')
  SEARCH        = (By.XPATH, '//nav//span[text()="Search"]')
  SEARCH_BAR    = (By.XPATH, '//nav//input[@placeholder="Search"]')
  
class SearchPageLocatars(object):
  NUM_LIKES         = (By.XPATH, '//a//ul//li[1]')
  NUM_COMMENTS      = (By.XPATH, '//a//ul//li[2]')
  NUM_VIEWS         = (By.XPATH, '//a//ul//li[1]')
  NUM_POSTS         = (By.XPATH, '//article//header//span[text()=" posts"]//span')
  POST_MOST_RECENT  = (By.XPATH, '//article//a//img')