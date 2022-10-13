
from base import PageBase

class HomePage(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)

    @classmethod
    def of(self, driver):
        return HomePage(driver=driver)

