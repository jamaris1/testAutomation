from selenium.webdriver.common.by import By

from tests.base.page_base import PageBase
import time
class HomePage(PageBase):
    
    t_shirt_element = "//div/following-sibling::ul/li/a[contains(@title, 'T-shirts')]"
    product_card_to_add = "//a[contains(text(), '{}')]/ancestor::li"
    product_to_add_button = product_card_to_add + "/descendant::span[contains(text(), 'Add to cart')]/ancestor::a"
    added_to_cart_message_element = "//i[contains(@class, 'ok')]/ancestor::h2"
    proceed_to_checkout_button = "//span[contains(text(), 'Proceed to checkout')]/ancestor::a"

    def __init__(self, driver):
        PageBase.__init__(self, driver)

    @classmethod
    def of(self, driver):
        return HomePage(driver=driver)

    def clickTShirts(self):
        self.click(self.t_shirt_element)
        return self

    def addProductToCart(self, text):
        self.scroll_into_view(self.product_card_to_add.format(text))
        self.move_to_element(self.product_card_to_add.format(text))
        self.click(self.product_to_add_button.format(text))
        return self
   
    def validateAddedMessage(self):
        self.scroll_into_view(self.added_to_cart_message_element)
        
        if self.driver.find_element(By.XPATH, self.added_to_cart_message_element):
            element = self.driver.find_element(By.XPATH, self.added_to_cart_message_element)
            text = element.text
            assert "Product successfully added to your shopping cart" in text
        return self

    def clickProceedToCheckout(self):
        self.click(self.proceed_to_checkout_button)
        return self