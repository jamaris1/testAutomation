
# new conde libraries
from selenium.webdriver.edge.options import Options as EdgeOptions
from msedge.selenium_tools import Edge, EdgeOptions
import datetime
# Original code libraries
import pytest
from webdriver_manager.chrome import ChromeDriverManager

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

from tests.page_objects.home_page import HomePage
from tests.page_objects.checkout_page import CheckOut

# Constants
 
HOME_URL = 'https://appxfaaifedev01.asexfadev01.appserviceenvironment.net/'
date = datetime.datetime.now()
date_string = date.strftime("%b-%d-%Y_%H%M%S")

# Scenarios
 
scenarios('../features/example.feature')
 
# Fixtures
@pytest.fixture
def driver():

    """
    Original code connection
    os.environ['WDM_SSL_VERIFY'] = '0'

    profile = webdriver.ChromeOptions()
    profile.add_argument('--ignore-certificate-errors')
    d = webdriver.Chrome(ChromeDriverManager().install())
    d.implicitly_wait(30)
    d.maximize_window()
    yield d
    d.quit()
    """
    PATH = 'C:\\Users\\YV5617\\PycharmProjects\\AutoTest\\venv\\Scripts\\msedgedriver.exe'

    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\YV5617\\AppData\\Local\\Microsoft\\Edge\\User_Data")
    #edge_options.add_argument("profile-directory=profil 1")


    driver = Edge(options=edge_options, executable_path=PATH)

    driver.implicitly_wait(50)
    driver.maximize_window()
    return driver
 
# Given Steps
@given("the automationpractice website is displayed")
def goToHomeWebsite(driver):
    HomePage.of(driver).goToURL(HOME_URL)


# When Steps
@when("l'utilisateur clique sur Configurer Connexion")
def clickOnConfigConnex(driver):
    HomePage.of(driver).clickConfigConnex()

 
@when(parsers.parse('il ajoute une nouvelle source de données "{test}" avec le port "{port}"'))
def fillSourceForm(driver, test, port):
    #HomePage.of(driver).addProductToCart(product).validateAddedMessage().clickProceedToCheckout()

    HomePage.of(driver).addSourceData(test+date_string, port)

# Then Steps
@then(parsers.parse('verifier que la source de données "{test}" est enregistrée'))
def validateSource(driver, test):
    HomePage.of(driver).validateConnCreation(test+date_string)

@when(parsers.parse('adds new extraction ZT "{product}"'))
def fillZTForm(driver, product):
    #HomePage.of(driver).addProductToCart(product).validateAddedMessage().clickProceedToCheckout()
    HomePage.of(driver).fill(product)

@when(parsers.parse('adds new extraction ZE "{product}"'))
def fillZEForm(driver, product):
    #HomePage.of(driver).addProductToCart(product).validateAddedMessage().clickProceedToCheckout()
    HomePage.of(driver).fill(product)

