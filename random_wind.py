import os 
import random 

def windscribe(action):
    windscribe_cli_path = r"C:\\Program Files\\Windscribe\\windscribe-cli.exe"
    connect_list = ["US Central", "US East", "US West","Best Location","Germany","France","Norway","Netherlands","Romania","United Kingdom","Turkey"]
    location = random.choice(connect_list)
    command = f'"{windscribe_cli_path}" {action} {location}'
    os.system(command)