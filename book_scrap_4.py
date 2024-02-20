from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains

def trova_num_pagine():
    wait = WebDriverWait(driver, 10)
    try: 
        numero_pagine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.a83ed08757.a2028338ea' )))
        numero_pagine = driver.find_elements(By.CSS_SELECTOR,'button.a83ed08757.a2028338ea')
        numero_pagine = int(numero_pagine[-1].text)
    except: numero_pagine = 1
    print("numero pagine da visitare:",numero_pagine)
    return numero_pagine

def close_genius():
    try:
        close_button = driver.find_elements(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]') 
        close_button[-1].click()
        time.sleep(1)
    except: pass

def sleep():
    sleeptime = random.uniform(2,5)
    time.sleep(sleeptime)

#per bypassare errore certificato
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--enable-javascript")

#chiedo in input città e date
citta = input("Citta:")
datain= input("Check-in:")
if len(datain)<1: datain = "2024-02-24"
dataout= input("Check-out:")
if len(dataout)<1: dataout = "2024-02-25"

userlist =["sunnytraveler@libero.it","pantilaura56@gmail.com"]
username = random.choice(userlist)
password = "Viaggiatore45!"

url = "https://www.booking.com/"
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get(url)
except:
    driver.quit()
try:
    wait = WebDriverWait(driver, 10)
    cookie_banner = wait.until(EC.visibility_of_element_located((By.ID,'onetrust-reject-all-handler' )))
    cookie_banner = driver.find_element(By.ID,'onetrust-accept-btn-handler')
    ActionChains(driver).move_to_element(cookie_banner).perform()
    cookie_banner.click()

except:
   pass
sleep()

close_genius()
#blocco che effettua accesso utente 
'''
try: 
    if username is None:
        pass
    else:
        accedi = driver.find_element(By.CSS_SELECTOR,'a[data-testid="header-sign-in-button"]')
        ActionChains(driver).move_to_element(accedi).perform()
        accedi.click()
        sleep()
        email = driver.find_element(By.CSS_SELECTOR,'input[type="email"]')
        ActionChains(driver).move_to_element(email).perform()
        email.click()
        for char in username: 
            email.send_keys(char)
            time.sleep(random.uniform(0.1,0.25))
        sleep()
        submit = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        ActionChains(driver).move_to_element(email).move_to_element(submit).click().perform()
        sleep()
        passw = driver.find_element(By.CSS_SELECTOR,'input[type="password"]')
        ActionChains(driver).move_to_element(passw).perform()
        passw.click()
        for char in password:
            passw.send_keys(char)
            time.sleep(random.uniform(0.1,0.25))
        sleep()
        submit = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        ActionChains(driver).move_to_element(passw).move_to_element(submit).click().perform()
        input("premi invio per continuare")
        driver.quit()
except:pass 
'''
try:     #eseguo ricerca
    search = driver.find_element(By.ID,':re:')
    for char in citta:
        search.send_keys(char)
        time.sleep(random.uniform(0.1,0.25))
    sleep()
    data = driver.find_element(By.CSS_SELECTOR,'div[data-testid="searchbox-dates-container"]')
    data.click()
    sleep()
    date = driver.find_element(By.CSS_SELECTOR,'span[data-date="'+datain+'"]')
    date.click()
    sleep()
    date = driver.find_element(By.CSS_SELECTOR,'span[data-date="'+dataout+'"]')
    date.click()
    sleep()
    button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    button.click()
except: 
    driver.quit()
    print("error")

sleep()

close_genius()
numero_pagine = trova_num_pagine()

dati_hotel=[]
html_content = ""
for pagina in range(numero_pagine):
    print("scansiono pagina:",pagina+1)
    sleep()
    close_genius()
    html = driver.page_source
    html_content += html +"/n/n"
    hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR,'div[data-testid=property-card]')
    for hotel in hotel_per_pagina:
        nome= hotel.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').text
        prezzo = hotel.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').text
        citta = hotel.find_element(By.CSS_SELECTOR, 'span[data-testid="address"]').text
        dati_hotel.append((nome,prezzo,citta,datain))
    #esco dal ciclo dopo che scansiono ultima pagina 
    if pagina == numero_pagine-1:
        break
    try:
        next_page = driver.find_element(By.CSS_SELECTOR,'button[aria-label="pagina successiva"]')
    except:
        driver.quit()
    #esco dal ciclo dopo che scansiono ultima pagina    
    
    next_page.click()

with open(citta+"-"+datain+".html", "w", encoding="utf-8") as file:
    file.write(html_content)

print(dati_hotel)  
print("Hotel scansionati",len(dati_hotel)) 

sleep()
driver.quit()
