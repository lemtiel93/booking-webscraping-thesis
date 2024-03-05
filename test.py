from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
import re 
import datetime

'''
chrome_options = webdriver.ChromeOptions(); 
#per bypassare errore certificato
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
url = "https://www.booking.com/"
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get(url)
except:
    print("ehi sono qua")
    #windscribe("disconnect")
    driver.quit()'''

'''ua = UserAgent(browsers=["chrome"])
fake_user_agent = ua.random
print(fake_user_agent)
regex  = "\s\((\w*)"
os = re.search(regex,fake_user_agent)
print(os.group(1))
if (os.group(1))=='X11':
    os='Linux'
elif(os.group(1))=='Macintosh':
    os='Mac'
else: pass

print(os)'''

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d---%H:%M")
print(now)





