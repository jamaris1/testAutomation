import pytest
from webdriver_manager.chrome import ChromeDriverManager
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from tests.page_objects.home_page import HomePage
from tests.page_objects.checkout_page import CheckOut

# Constants
 
HOME_URL = 'http://automationpractice.com/index.php'
 
# Scenarios
 
scenarios('../features/example.feature')
 
# Fixtures
@pytest.fixture
def driver():
    d = webdriver.Chrome(ChromeDriverManager().install())
    d.implicitly_wait(30)
    d.maximize_window()
    yield d
    d.quit()
 
# Given Steps
@given("the automationpractice website is displayed")
def goToHomeWebsite(driver):
    HomePage.of(driver).goToURL(HOME_URL)


# When Steps
@when("the user clicks on TShirts")
def clickOnTShirtsButton(driver):
    HomePage.of(driver).clickTShirts()
 
@when(parsers.parse('adds to the cart the "{product}"'))
def addToCart(driver, product):
    HomePage.of(driver).addProductToCart(product).validateAddedMessage().clickProceedToCheckout()

# Then Steps
@then("the user is redirected to checkout")
def validateRedirected(driver):
    CheckOut.of(driver).validatePageIsCheckout()