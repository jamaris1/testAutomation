
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains




class PageBase(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.action = ActionChains(self.driver)

    @classmethod
    def of(driver):
        return PageBase(driver=driver)

    def goToURL(self, url):
        self.driver.get(url)
        return self
