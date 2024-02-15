from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
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

def clean_text(text):
    '''Extract only the temperature from text'''
    output = float(text.split(': ')[1])
    return output

def main(path):
    driver = get_driver('http://automated.pythonanywhere.com/')
    time.sleep(3)
    # element = driver.find_element(By.XPATH,value='/html/body/div[1]/div/h1[1]')
    element = driver.find_element(by='xpath',value=f'{path}')
    return clean_text(element.text)

print(main('/html/body/div[1]/div/h1[2]'))