import random

def get_random_user_agent(choice):
    if choice == 0:  # Se è scelto un dispositivo mobile
        user_agents = [
            # Samsung Galaxy S22 5G
            "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
            # iPhone 13 Pro Max
            #"Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
        ]
    elif choice == 1:  # Se è scelto un dispositivo desktop
        # PER FUNZIONARE DEVI ESSERE A SCHERMO INTERO SENNO CREDE DI ESSERE SU MOBILE
        user_agents = [
            # Windows 10-based PC using Edge browser (Questa funziona alla grande)
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            # Chrome OS-based laptop using Chrome browser (Chromebook) (COME SE FOSSE VERSIONE MOBILE)
            "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
            # Mac OS X-based computer using a Safari browser (COME SE FOSSE VERSIONE MOBILE)
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
            # Windows 7-based PC using a Chrome browser (COME SE FOSSE VERSIONE MOBILE)
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
            # Linux-based PC using a Firefox browser (COME SE FOSSE VERSIONE MOBILE)
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        ]
    else:
        raise ValueError("La scelta deve essere 0 per mobile o 1 per desktop")

    random_index = random.randint(0, len(user_agents) - 1)
    return user_agents[random_index]
