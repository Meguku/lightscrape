from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import wget, random, string
import os, selenium, time

os.chdir(os.getcwd()+"/lightscrape")
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
webdriver = os.getcwd()+"/chromedriver"

BASE_URL = 'https://prnt.sc/'
lower_alphabet = string.ascii_lowercase
def randNL():
    list = []
    for i in range(6):
        choise = random.randint(0,1)
        if choise == 0:
            int = random.randint(0,9)
            list.append(int)
        else:
            letter = random.choice(lower_alphabet)
            list.append(letter)
    END_URL = ''.join(map(str, list))
    #print(END_URL)
    return END_URL
   

os.chdir(os.getcwd()+'/photos')
while True:
    driver = Chrome(chrome_options=chrome_options, executable_path=webdriver)
    while True:
        driver.get(BASE_URL+randNL())
        try:
            img = driver.find_element_by_id('screenshot-image').get_attribute('src')
            if img.__contains__('imgur'):
                wget.download(img)
        except selenium.common.exceptions.NoSuchElementException:
            print('\nelement not found')