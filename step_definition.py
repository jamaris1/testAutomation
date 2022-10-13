
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from home import HomePage

HOME_URL = 'http://automationpractice.com/index.php'


def goToHomeWebsite(driver):
    HomePage.of(driver).goToURL(HOME_URL)



def driver():
    # Combines the Selenium and Webdriver_Manager library to install the webdriver.
    #PATH = 'C:\\Users\\jaime.amaris\\.wdm\drivers\\chromedriver\\win32\\105.0.5195\\chromedriver.exe'
    #d = webdriver.Chrome(PATH)


    d = webdriver.Chrome(ChromeDriverManager().install())
    #d.implicitly_wait(30)
    #d.maximize_window()
    # it is like a return keyword but as soon as a yield is encountered, the execution of the function halts and returns a generator iterator object instead of simply returning a value.
    #yield d
    #d.quit()
    return d





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello')

    d = driver()
    goToHomeWebsite(d)



