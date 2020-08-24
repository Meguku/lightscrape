from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import wget, random, string, os, selenium, sys, platform

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

BASE_URL = 'https://prnt.sc/'
lower_alphabet = string.ascii_lowercase

if platform.system() == 'Windows':
    webdriver = "chromedriver.exe"
elif platform.system() == 'Linux':
    webdriver = "chromedriver"
else:
    print("Not supported OS. (Only Windows and Linux)")

driver = Chrome(options=options, executable_path=webdriver)

try:
    os.mkdir('shots')
except:
    print('Dir "shots" exists')
finally:
    os.chdir('shots')

def randNL():
    list = []
    for i in range(6):
        choise = random.randint(0,1)
        if choise == 0:
            list.append(random.randint(0,9))
        else:
            list.append(random.choice(lower_alphabet))
    END_URL = ''.join(map(str, list))
    return END_URL

def main(i):
    for n in range(int(i)):
        while True:
            driver.get(BASE_URL+randNL())
            try:
                img = driver.find_element_by_id('screenshot-image').get_attribute('src')
                if img.__contains__('imgur'):
                    print('\n{}.'.format(str(n+1)))
                    wget.download(img)
                    break
            except selenium.common.exceptions.NoSuchElementException:
                print('\nElement not found')

if __name__ == "__main__":
    main(sys.argv[1])
