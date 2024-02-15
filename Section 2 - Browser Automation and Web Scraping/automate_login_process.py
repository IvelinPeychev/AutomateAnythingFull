from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

def login():
    driver = get_driver('http://automated.pythonanywhere.com/login/')
    driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys('automated')
    time.sleep(2)
    # driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys('automatedautomated')
    # driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/form/button').click()
    # element = driver.find_element(by='xpath',value=f'{path}')

    # Instead of locate the login button we can use the KEYS and ENTER directly after entering the password
    driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys('automatedautomated' + Keys.ENTER)
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(by='xpath',value='/html/body/nav/div/a').click()
    print(driver.current_url)


login()

