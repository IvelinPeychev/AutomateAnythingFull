from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# If the driver path is not in ENV PATH
# service = Service('E:\Education\Auto\webdrivers_new\chromedriver.exe')



def get_driver(url):
    # Set option to make browser easier to use
    options = webdriver.ChromeOptions()

    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options)
    driver.get(url)
    return driver

def main(path):
    driver = get_driver('http://automated.pythonanywhere.com/')
    # element = driver.find_element(By.XPATH,value='/html/body/div[1]/div/h1[1]')
    element = driver.find_element(by='xpath',value=f'{path}')
    return element.text

print(main('/html/body/div[1]/div/h1[1]'))