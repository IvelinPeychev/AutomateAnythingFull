from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

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
    # login user and password
    driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys('automated')
    driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys('automatedautomated' + Keys.ENTER)

    # Click home button
    driver.find_element(by='xpath',value='/html/body/nav/div/a').click()

    time.sleep(2)
    # Scrape the temp
    element = driver.find_element(by='xpath',value='/html/body/div[1]/div/h1[2]/div')
    temp_txt = element.text.split(': ' )[1]
    return temp_txt

def main():
    while True:
        time.sleep(2)
        result = login()
        filename = f'{datetime.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt'
        with open(filename, 'w') as f:
            f.write(result)

main()