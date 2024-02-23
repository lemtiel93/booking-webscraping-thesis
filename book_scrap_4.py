from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

#per inserire lo useragent
from selenium.webdriver.chrome.options import Options

from user_agent import get_random_user_agent

from selenium.webdriver import ActionChains

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
choice = int(input("Inserisci 0 per dispositivo mobile o 1 per dispositivo desktop: "))
fake_user_agent = get_random_user_agent(choice)
print("User Agent casuale:", fake_user_agent)

############################### TODO per ora disattivato
#windscribe("connect")
###############################
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_argument(f'user-agent={fake_user_agent}')
#per bypassare errore certificato
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--enable-javascript")

#chiedo in input città e date asdasd
citta = input("Citta:")
if len(citta)<1: citta = "Palermo"
datain= input("Check-in:")
if len(datain)<1: datain = "2024-02-28"
dataout= input("Check-out:")
if len(dataout)<1: dataout = "2024-02-29"

userlist =["sunnytraveler@libero.it","pantilaura56@gmail.com"]
username = random.choice(userlist)
password = "Viaggiatore45!"

url = "https://www.booking.com/"
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get(url)
except:
    print("ehi sono qua")
    #windscribe("disconnect")
    driver.quit()

#INIZIARE QUA DISTINZIONE FRA MOBILE E DESKTOP
#   1 -> desktop . 0 -> mobile
    
if choice == 1 :
    print("desktop!")
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
        print("non trovo i dati barra di ricerca")
        #windscribe("disconnect")
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
            #SIA PUNTEGGIO CHE NUM_RECENSIONI POSSONO NON ESSERCI IN CASO DI NUOVO CLIENTE 
            #PUNTEGGIO TRAMITE IL DIV a3b8729ab1 d86cee9b25
            try:
                # Prova a estrarre il punteggio se presente
                punteggio = hotel.find_element(By.CSS_SELECTOR, 'div[class="a3b8729ab1 d86cee9b25"]').text
            except NoSuchElementException:
                print("nessun punteggio")
                punteggio = None
                pass
            #NUMERO RECENSIONI TRAMITE IL DIV  abf093bdfe f45d8e4c32 d935416c47
            try:
                # Prova a estrarre il numero di recensioni se presente
                num_recensioni = hotel.find_element(By.CSS_SELECTOR, 'div[class="abf093bdfe f45d8e4c32 d935416c47"]').text
            except NoSuchElementException:
                print("nessun num_recensioni")
                num_recensioni = None
                pass
            #DISTANZA DAL CENTRO
            distanza_centro = hotel.find_element(By.CSS_SELECTOR, 'span[data-testid="distance"]').text
            dati_hotel.append((nome,prezzo,citta,datain,punteggio,num_recensioni,distanza_centro))
            #print di check
            #print(dati_hotel)
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

elif choice == 0 :
    print("telefono!")
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

    try:     #eseguo ricerca mobile
        search = driver.find_element(By.ID,':r8:')
        search.click()
        for char in citta:
            search.send_keys(char)
            time.sleep(random.uniform(0.1,0.25))
        close_city = driver.find_element(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]')
        close_city.click()
        sleep()
        data = driver.find_element(By.CSS_SELECTOR,'button[class="b8118a93a7"]')
        data.click()
        sleep()
        sleep()
        sleep()
        date = driver.find_element(By.CSS_SELECTOR,'span[data-date="'+datain+'"]')
        date.click()
        sleep()
        date = driver.find_element(By.CSS_SELECTOR,'span[data-date="'+dataout+'"]')
        date.click()
        sleep()
        # click fatto dopo scelta data -- init
        btn_fatto = driver.find_element(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982"]')
        btn_fatto.click()
        # click fatto -- end
        sleep()
        button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        button.click()
    except: 
        print("non trovo i dati barra di ricerca")
        #windscribe("disconnect")
        driver.quit()
        print("error")

    sleep()
    sleep()

    close_genius()

    hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR,'div[data-testid=property-card]')
    print(len(hotel_per_pagina))  # Utilizzo len() per ottenere la lunghezza della lista cioè il numero di card hotel
    
    sleep()
    sleep()

    while True:
        if len(hotel_per_pagina) < 80 :
            # Trova tutti gli elementi degli hotel attualmente visualizzati
            hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid=property-card]')
        
            # Stampa il numero di hotel trovati finora
            print("Numero totale di hotel trovati FINORA:", len(hotel_per_pagina))

            # Scrolla verso il basso per caricare ulteriori hotel
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Attendi un po' di tempo per il caricamento degli hotel
            time.sleep(5)  # Modifica il tempo di attesa a seconda della tua velocità di connessione e del tempo di caricamento della pagina
        else : 
            break
            print("SEI USCITO DAI PRIMI 90 : ", len(hotel_per_pagina))
            try :
                # Attendi un po' di tempo per il caricamento degli hotel
                time.sleep(5)  # Modifica il tempo di attesa a seconda della tua velocità di connessione e del tempo di caricamento della pagina
                btn_carica = driver.find_element(By.XPATH, "//span[text()='Carica più risultati']")
                # Crea un oggetto ActionChains
                action = ActionChains(driver)
                # Muoviti sull'elemento del bottone
                action.move_to_element(btn_carica).perform()
                # Attendi un po' di tempo per il caricamento degli hotel
                time.sleep(5)  # Modifica il tempo di attesa a seconda della tua velocità di connessione e del tempo di caricamento della pagina
                btn_carica.click()
                # Attendi un po' di tempo per il caricamento degli hotel
                time.sleep(5)  # Modifica il tempo di attesa a seconda della tua velocità di connessione e del tempo di caricamento della pagina
                # Trova tutti gli elementi degli hotel attualmente visualizzati
                hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid=property-card]')
            except NoSuchElementException:
                hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid=property-card]')
                print("Non ci sono più hotel da caricare.")
                break
    dati_hotel = []
    print(hotel_per_pagina)
    print(len(hotel_per_pagina))
    for hotel in hotel_per_pagina:
        nome= hotel.find_element(By.CSS_SELECTOR,'a[data-testid="title"]').text
        prezzo = hotel.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').text
        citta = hotel.find_element(By.CSS_SELECTOR, 'span[class="afad290af2"]').text
        #SIA PUNTEGGIO CHE NUM_RECENSIONI POSSONO NON ESSERCI IN CASO DI NUOVO CLIENTE 
        #PUNTEGGIO TRAMITE IL DIV a3b8729ab1 d86cee9b25
        try:
            # Prova a estrarre il punteggio se presente
            punteggio = hotel.find_element(By.CSS_SELECTOR, 'div[class="abf093bdfe d86cee9b25"]').text
        except NoSuchElementException:
            print("nessun punteggio")
            punteggio = None
            pass
        #NUMERO RECENSIONI TRAMITE IL DIV  abf093bdfe f45d8e4c32 d935416c47
        try:
            # Prova a estrarre il numero di recensioni se presente
            num_recensioni = hotel.find_element(By.CSS_SELECTOR, 'span[class="abf093bdfe f45d8e4c32 d935416c47"]').text
        except NoSuchElementException:
            print("nessun num_recensioni")
            num_recensioni = None
            pass
        #DISTANZA DAL CENTRO
        distanza_centro = citta.split("•")[1]
        citta = citta.split("•")[0]
        dati_hotel.append((nome,prezzo,citta,datain,punteggio,num_recensioni,distanza_centro))
        #print di check
        #print(dati_hotel)
    print(dati_hotel)


else :
    print("error")