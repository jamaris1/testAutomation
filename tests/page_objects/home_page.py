from selenium.webdriver.common.by import By

from tests.base.page_base import PageBase
import time
class HomePage(PageBase):
    
    config_connex_element = "//button[contains(@title, 'Configurer une source de données')]"
    add_connex_element = "//button[contains(@id, 'btn-new-connection')]"
    enregist_conn_element = "//button[contains(@id,'saveBtn')]"
    Search_connex_element = "//input[contains(@id, 'control-panel')]"


    inputSearch_connex_id = "//input[contains(@class, 'p-listbox-filter p-inputtext p-component')]"
    input_connex_id = "//input[contains(@id,'field-1-nom-source')]"
    input_server_id = "//input[contains(@id,'field-1_server')]"
    input_bd_id = "//input[contains(@id,'field-1_database')]"
    input_port_no = "//input[contains(@id,'field-1_port')]"
    input_schema_nom = "//input[contains(@id,'field-1_schema')]"
    input_log_in = "//input[contains(@id,'field-1_login')]"
    input_secr_et = "//input[contains(@id,'field-1_secret')]"

    succ_message = "//h5[contains(@_ngcontent-uel-c97,'')]"



    product_card_to_add = "//input[contains(@id, field-2-nom-source)]"
    product_to_add_button = product_card_to_add + "/descendant::span[contains(text(), 'Add to cart')]/ancestor::a"
    added_to_cart_message_element = "//i[contains(@class, 'ok')]/ancestor::h2"
    proceed_to_checkout_button = "//span[contains(text(), 'Proceed to checkout')]/ancestor::a"

    #/ html / body / app - root / div / main / div / app - configurer / app - main - layout / app - toast - message / p - toast / div / p - toastitem / div / div / div / div
    #< div
    #_ngcontent - uel - c97 = ""

    #class ="toast-content p-text-center" > < !----> < i _ngcontent-uel-c97="" class ="fa-plug fas ng-star-inserted" > < / i > < !----> < h5 _ngcontent-uel-c97="" > Paramètres de connexion enregistrés avec succès! < / h5 > < / div >

    def __init__(self, driver):
        PageBase.__init__(self, driver)

    @classmethod
    def of(self, driver):
        return HomePage(driver=driver)

    def clickConfigConnex(self):
        self.click(self.config_connex_element)
        self.click(self.add_connex_element)
        #self.click(self.input_connex_id)
        time.sleep(10)

        return self

    def addSourceData(self, test, port):
        self.fill(self.input_connex_id,test)
        self.fill(self.input_server_id,test)
        self.fill(self.input_bd_id,test)
        self.fill(self.input_port_no,port)
        self.fill(self.input_schema_nom,test)
        self.fill(self.input_log_in,test)
        self.fill(self.input_secr_et,test)
        self.click(self.enregist_conn_element)
        time.sleep(20)



        return self


    def validateConnCreation(self, test):
        self.fill(self.inputSearch_connex_id,test)
        
        time.sleep(20)

        return self

    def clickProceedToCheckout(self):
        self.click(self.proceed_to_checkout_button)
        return self