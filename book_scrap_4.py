from random_wind import windscribe
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def trova_num_pagine():
    wait = WebDriverWait(driver, 10)
    try: 
        numero_pagine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.a83ed08757.a2028338ea' )))
        numero_pagine = driver.find_elements(By.CSS_SELECTOR,'button.a83ed08757.a2028338ea')
        numero_pagine = int(numero_pagine[-1].text)
    except: numero_pagine = 1
    print("numero pagine da visitare:",numero_pagine)
    return numero_pagine

windscribe("connect")
#per bypassare errore certificato
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_experimental_option("detach", True)

#chiedo in input città e date asdasd
citta = input("Citta:")
datain= input("Check-in:")
if len(datain)<1: datain = "2024-02-20"
dataout= input("Check-out:")
if len(dataout)<1: dataout = "2024-02-25"

url = "https://www.booking.com/"
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get(url)
except:
    windscribe("disconnect")
    driver.quit()

try:
    wait = WebDriverWait(driver, 10)
    cookie_banner = wait.until(EC.visibility_of_element_located((By.ID,'onetrust-reject-all-handler' )))
    cookie_banner = driver.find_element(By.ID,'onetrust-reject-all-handler').click() 
except:
   pass
time.sleep(4)
try: #qui chiudo un pop-up dove suggerisce di registrarsi
    close_button = driver.find_element(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]') 
    close_button.click()
except:
    pass 

try:     #qualora non avesse funzionato agisco sulla barra di ricerca
    search = driver.find_element(By.ID,':re:')
    search.send_keys(citta)
    time.sleep(2)
    data = driver.find_element(By.CSS_SELECTOR,'div[data-testid="searchbox-dates-container"]')
    data.click()
    time.sleep(2)
    date = driver.find_element(By.CSS_SELECTOR,'span[data-date="'+datain+'"]')
    date.click()
    time.sleep(2)
    date = driver.find_element(By.CSS_SELECTOR,'span[data-date="'+dataout+'"]')
    date.click()
    time.sleep(2)
    button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    button.click()
    numero_pagine = trova_num_pagine()
except: 
    windscribe("disconnect")
    driver.quit()
    print("error")

dati_hotel=[]
for pagina in range(numero_pagine):
    print("scansiono pagina:",pagina+1)
    time.sleep(4)
    try:
        close_button = driver.find_elements(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]') 
        close_button[-1].click()
    except: pass
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
        windscribe("disconnect")
        driver.quit()
    #esco dal ciclo dopo che scansiono ultima pagina    
    
    next_page.click()

print(dati_hotel)  
print("Hotel scansionati",len(dati_hotel)) 

time.sleep(5)
windscribe("disconnect")
driver.quit()