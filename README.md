# Webscraping per l'Analisi delle Discriminazioni di Prezzo su Booking.com

## Introduzione

Questo progetto utilizza tecniche di webscraping per analizzare e confrontare i prezzi degli hotel su Booking.com in base a diversi fattori, come il dispositivo utilizzato per l'accesso al sito web, l'utilizzo di una VPN e altri parametri. Lo scopo principale di questo progetto è dimostrare la presenza di eventuali discriminazioni di prezzo in base a tali fattori.

## Cenni

### Webscraping

Il webscraping è una tecnica utilizzata per l'estrazione di dati da siti web. Consiste nell'analizzare la struttura di una pagina web e quindi estrarre le informazioni desiderate attraverso l'accesso diretto al codice HTML della pagina. In questo progetto, il webscraping viene utilizzato per estrarre i prezzi degli hotel e altre informazioni pertinenti da Booking.com.

### Discriminazioni di Prezzo

Le discriminazioni di prezzo si verificano quando gli stessi prodotti o servizi vengono offerti a prezzi diversi a diversi gruppi di consumatori, senza una giustificazione razionale. In questo contesto, ci si propone di verificare se esistono differenze significative nei prezzi degli hotel su Booking.com in base a vari fattori, come il dispositivo utilizzato per accedere al sito o l'utilizzo di una VPN.

## Librerie Utilizzate

- **Selenium**: Utilizzata per l'automazione del browser web e il webscraping.
- **Fake User-Agent**: Utilizzata per generare user-agent casuali, simulando l'accesso da diversi dispositivi.
- **WebDriverManager**: Utilizzata per gestire automaticamente i driver del browser web.
- **random_wind**: Utilizzata per la gestione della connessione tramite Windscribe (ATTENZIONE: attualmente disattivata).

## Motivazioni per l'utilizzo delle librerie

- **selenium** Essenziale per l'automazione del browser, necessaria per eseguire ricerche e navigare su Booking.com.
- **fake_useragent**: Utilizzata per fornire user agent casuali ai fini della simulazione di dispositivi variabili, utile per evitare la rilevazione automatizzata e ottenere risultati più accurati durante la scansione degli hotel.

## Flow dell'Algoritmo

1. **Generazione del Fake User-Agent**: Viene generato un user-agent casuale per simulare l'accesso da diversi dispositivi.
2. **Connessione al Sito Web**: Viene aperto un browser web utilizzando Selenium e il fake user-agent generato.
3. **Accesso a Booking.com**: Il browser naviga su Booking.com per iniziare la ricerca degli hotel.
4. **Estrazione dei Dati**: Utilizzando tecniche di webscraping, vengono estratti i prezzi degli hotel e altre informazioni pertinenti.
5. **Analisi dei Dati**: I dati estratti vengono analizzati per identificare eventuali differenze nei prezzi degli hotel in base ai fattori considerati.
6. **Chiusura del Browser**: Una volta completata l'analisi, il browser viene chiuso.

## Note aggiuntive

- Assicurati di avere un'installazione funzionante di Chrome e i driver di Selenium corrispondenti.
- Assicurati di rispettare i termini di servizio di Booking.com e di non utilizzare questo programma per scopi non etici o non autorizzati.
- ATTENZIONE: La connessione tramite Windscribe è disattivata per il momento. Se necessario, può essere riattivata modificando il codice.
