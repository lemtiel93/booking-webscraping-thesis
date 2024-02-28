from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
#FAKEUSERAGENT per simulare dispositivi
from fake_useragent import UserAgent
#per inserire lo useragent
from selenium.webdriver.chrome.options import Options
from user_agent import get_random_user_agent
import datetime

def trova_num_pagine():
    wait = WebDriverWait(driver, 5)
    try: 
        numero_pagine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.a83ed08757.a2028338ea' )))
        numero_pagine = driver.find_elements(By.CSS_SELECTOR,'button.a83ed08757.a2028338ea')
        numero_pagine = int(numero_pagine[-1].text)
    except: numero_pagine = 0
    print("numero pagine da visitare:",numero_pagine)
    return numero_pagine


def close_genius():
    try:
        close_button = driver.find_elements(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]') 
        close_button[-1].click()
        time.sleep(2)
    except: pass

def sleep():
    sleeptime = random.uniform(3,5)
    time.sleep(sleeptime)

def estrai_hotel(dati):
    hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR,'div[data-testid=property-card]')
    for hotel in hotel_per_pagina:
        html_content_list.append(hotel.get_attribute("outerHTML"))
        nome= hotel.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').text
        stanza = hotel.find_element(By.CSS_SELECTOR,'h4[role="link"]').text
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
        try:
            #prova a vedere se hotel è genius
            hotel.find_element(By.CSS_SELECTOR,'span[data-testid="genius-badge"]')
            genius = True
        except NoSuchElementException:
            genius = False
        try:
            #vedo se colazione è inclusa
            hotel.find_element(By.CSS_SELECTOR,'span[class="a19404c4d7"]')
            colazione_inclusa = True
        except NoSuchElementException:
            colazione_inclusa = False  
        try:
            #pagamento anticipato e cancellazione gratuita
            info_varie = hotel.find_elements(By.CSS_SELECTOR,'strong')
            stringa_informazioni=""
            for i in info_varie:
                stringa_informazioni += i.text +" "
        except NoSuchElementException:
            stringa_informazioni = None
        try:
            #offerte presenti su un hotel
            card_deal = hotel.find_elements(By.CSS_SELECTOR,'span[data-testid="property-card-deal"]')
            deal=""
            for i in card_deal:
                deal += i.find_element(By.CSS_SELECTOR,'span[class="b30f8eb2d6"]').text + " "
        except NoSuchElementException:
            deal = None
        dati.append((nome,prezzo,stanza,citta,datain,punteggio,num_recensioni,distanza_centro,genius,deal,colazione_inclusa,stringa_informazioni,os,username,now2))

def crea_html():
    with open(citta+"-"+datain+"-"+username+"-"+now+".html", "w", encoding="utf-8") as file:
        file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Html Content</title>\n</head>\n<body>\n")
        for html_content in html_content_list:
            file.write(html_content + "\n")
        file.write("</body>\n</html>")


#per bypassare errore certificato

# CHECK DESKTOP O MOBILE
choice = int(input("Inserisci 0 per dispositivo mobile o 1 per dispositivo desktop: "))
if choice == 0 :
    fake_user_agent = get_random_user_agent(choice)

elif choice == 1 :
    # Creare un'istanza di UserAgent
    ua = UserAgent(browsers=["chrome"])
    fake_user_agent = ua.random

print(fake_user_agent)

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_argument(f'user-agent={fake_user_agent}')
#per bypassare errore certificato
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--start-maximized')
#chrome_options.add_argument("--enable-javascript")
#chrome_options.add_argument("--clear-data")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

#chiedo in input città e date 
citta = input("Citta:")
datain= input("Check-in:")
if len(datain)<1: datain = "2024-03-05"
dataout= input("Check-out:")
if len(dataout)<1: dataout = "2024-03-06"

start_time = time.time()
#ottengo data e orario in cui ho effettuato ricerca
now = datetime.datetime.now()
now = now.strftime("%m-%d---%H-%M")

#ottengo data e orario in cui ho effettuato ricerca
now2 = datetime.datetime.now()
now2 = now2.strftime("%m-%d-%YYYY---%H:%M")

userlist =["sunnytraveler@libero.it","pantilaura56@gmail.com","marcofantile@proton.me"]
username = random.choice(userlist)
password = "Viaggiatore45!"

url = "https://www.booking.com/"
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get(url)
except:
    print("ehi sono qua")
    #windscribe("disconnect")
    #
    driver.quit()

#LATO DESKTOP
if choice == 1 :

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
            sleep()
    except:pass 

    username = username.split('@')[0]
    sleep()
    try:     #eseguo ricerca
        search = driver.find_element(By.CSS_SELECTOR,'input[name="ss"]')
        for i in range(12):
            search.send_keys(Keys.BACK_SPACE)
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

    regex  = r"\s\((\w*)"
    os = re.search(regex,fake_user_agent)
    if (os.group(1))=='X11':
        os='Linux'
    elif(os.group(1))=='Macintosh':
        os='MacOS'
    else: os='Windows'

    dati_hotel = []
    #creo header per i dati
    dati_hotel.append(("nome_hotel","prezzo","stanza","città","data","punteggio","numero_recensioni","distanza_centro","genius","offerte","colazione_inclusa","info_varie","os","username","TIMESTAMP"))  
    html_content_list=[]
    for pagina in range(numero_pagine):
        print("scansiono pagina:",pagina+1)
        sleep()
        time.sleep(1)
        close_genius()
        estrai_hotel(dati_hotel)
            #print di check
            #print(dati_hotel)
        #esco dal ciclo dopo che scansiono ultima pagina 
        if pagina == numero_pagine-1:
            break
        try:
            next_page = driver.find_element(By.CSS_SELECTOR,'button[aria-label="pagina successiva"]')
        except:
            print("sono uscito qui")
            driver.quit()
            break
        #esco dal ciclo dopo che scansiono ultima pagina    
        
        next_page.click()
    #creo il file html inserendo il nome utente nel titolo  

    if (numero_pagine==0):
        while True:
            #scorro verso il basso la pagina
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep()
            #cerco il pulsante che carica altri hotel finchè esiste
            try:
                wait = WebDriverWait(driver, 10)
                numero_pagine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 bf0537ecb5 f671049264 deab83296e af7297d90d"]' )))
                load_button = driver.find_element(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 bf0537ecb5 f671049264 deab83296e af7297d90d"]')
                load_button.click()
                sleep()
            except: 
                break
        #estraggo tutti i dati
        estrai_hotel(dati_hotel)
        crea_html()
    else:
        crea_html()
        


    print(dati_hotel) 
    print("Hotel scansionati",len(dati_hotel)-1) 

    try:
        df = pd.read_csv(citta+"_dati_booking.csv")
        df2 = pd.DataFrame(dati_hotel,columns=df.columns)
        df2 = df2.iloc[1:]
        df3 = pd.concat([df,df2],ignore_index=True)
        df3.to_csv(citta+"_dati_booking.csv",index = False)
    except:
        df = pd.DataFrame(dati_hotel)
        df.to_csv(citta+"_dati_booking.csv",index = False,header = False)

    #df = pd.DataFrame(dati_hotel)
    #df.to_csv("dati_booking.csv",index = False,header = False)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo trascorso:", execution_time, "secondi.")

    sleep()
    driver.quit()

#LATO MOBILE
elif choice == 0 :
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
    input("331")
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

    close_genius()

    hotel_per_pagina = driver.find_elements(By.CSS_SELECTOR,'div[data-testid=property-card]')
    print(len(hotel_per_pagina))  # Utilizzo len() per ottenere la lunghezza della lista cioè il numero di card hotel

    sleep()
    if_count = 0
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
            if_count += 1
            # Esce dal ciclo se ci sono meno di 80 strutture
            if (if_count == 4):
                break    
        else : 
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
        #dati_hotel.append(("nome_hotel","prezzo","stanza","città","data","punteggio",
        #"numero_recensioni","distanza_centro","genius","offerte","colazione_inclusa","info_varie","os","username","orario_ricerca"))  
        # genius -> se hotel è genius -> devi avere effettuato il login -> True->si  o False->no
        # offerte -> offerte di booking paga o super segrete #TODO DA VEDERE SE SI PUò DIVIDERE IN PIU COLONNE CON BOOLEANI
        # LO FACCIAMO SU PANDAS
        # colazione_inclusa -> se c'è o meno : TRUE->si O FALSE->no 
        # info_varie -> cancellazione gratuita o pagamento in struttura #TODO DA VEDERE SE SI PUò DIVIDERE IN PIU COLONNE CON BOOLEANI
        # LO FACCIAMO SU PANDAS
        # os -> sistema operativo della ricerca
        # username -> mail di ricerca
        # orario_ricerca -> timestamp     #TODO 02-28-2024---17:47 FARE NOW2
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
    driver.quit()
