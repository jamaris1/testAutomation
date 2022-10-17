import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from tests.base.customEC import wait_for_page_to_load

class PageBase(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.action = ActionChains(self.driver)

    @classmethod
    def of(driver):
        return PageBase(driver=driver)

    def wait_for_page(self):
        time.sleep(5)
        self.wait.until(wait_for_page_to_load, True)

    def wait_for_element(self, locator):
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def scroll_into_view(self, locator):
        self.wait_for_page()
        self.wait_for_element(locator)
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def move_to_element(self, locator):
        self.wait_for_page()
        self.wait_for_element(locator)
        element = self.driver.find_element(By.XPATH, locator)
        self.action.move_to_element(element).perform()

    def goToURL(self, url):
        self.driver.get(url)
        return self

    def click(self, locator):
        self.wait_for_page()
        self.wait_for_element(locator)
        self.driver.find_element(By.XPATH, locator).click()
        return self

    def fill(self, locator, text):
        self.wait_for_page()
        self.wait_for_element(locator)
        self.scroll_into_view(locator)
        self.driver.find_element(By.XPATH, locator).send_keys(text)
        return self