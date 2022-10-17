from selenium.webdriver.common.by import By

from tests.base.page_base import PageBase

class CheckOut(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)

    @classmethod
    def of(self, driver):
        return CheckOut(driver=driver)

    def validatePageIsCheckout(self):
        self.wait_for_page()
        url = self.driver.current_url
        assert "controller=order" in url