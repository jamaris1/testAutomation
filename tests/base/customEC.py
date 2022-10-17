from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException as staleExcp

class wait_for_page_to_load(object):

    def __init__(self, driver):
        self.driver = driver

    def __call__(self):
        try:
            docState = self.driver.execute_script("return document.readyState")
            return docState == 'complete'
        except staleExcp:
            return False