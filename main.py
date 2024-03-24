"""
Name: Duino-Coin Data Viewer
Author: ByteBoss
Data Time: 24/03/2024
Description: This script displays a user's Duino-Coin account data., This script displays the data of a user's Duino-Coin account.
"""

import requests
import time
import os
from colorama import Fore, Style



def clear_screen():
    # Comando para limpiar la pantalla en diferentes sistemas operativos
    if os.name == 'nt': # Windows
        _ = os.system('cls')
    else: # Linux y Mac
        _ = os.system('clear')

def get_duco_data(wallet_address):
    url = f"https://server.duinocoin.com/users/{wallet_address}"
    response = requests.get(url)
    return response.json()
    
def main():
    usuario = input("Enter your username: ")
    tiempo = int(input("Enter the time of refresh (in seconds): "))
    wallet_address = usuario
    
    while True:
        data = get_duco_data(wallet_address)
        if data:
            
            
            print("***************************************************************")
            print("Miners:")
            for i in range(len(data['result']['miners'])):
                print("==============================================================================================")
                print(Fore.BLUE + "Miner name: " + Style.RESET_ALL + f"{data['result']['miners'][i]['identifier']}")
                print(Fore.YELLOW + "Hashrate: " + Style.RESET_ALL + F"{data['result']['miners'][i]['hashrate']}")                  
                print(Fore.MAGENTA +"Diff: " + Style.RESET_ALL + f"{data['result']['miners'][i]['diff']}")                 
                print(Fore.CYAN + "Software: " + Style.RESET_ALL + f"{data['result']['miners'][i]['software']}")
                print("==============================================================================================")  
            print("***************************************************************")
            print("###############################################################")
            print("Transactions:")
            for i in range(len(data['result']['transactions'])):
                print("........................................................")
                print(Fore.GREEN + "Sender: " + Style.RESET_ALL + f"{data['result']['transactions'][i]['sender']}")
                print(Fore.YELLOW + "Amount: " + Style.RESET_ALL +  f"{data['result']['transactions'][i]['amount']}")
                print(Fore.CYAN + "Data Time: " + Style.RESET_ALL + f"{data['result']['transactions'][i]['datetime']}")
                print(Fore.MAGENTA + "Memo: "  + Style.RESET_ALL +  f"{data['result']['transactions'][i]['memo']}")
                print("........................................................")
            print("###############################################################")
            print("---------------------------------------------------------------")
            print(Fore.CYAN + "Username: " + Style.RESET_ALL + f"{data['result']['balance']['username']}")
            print(Fore.GREEN + "Balance: "  + Style.RESET_ALL +  f"{data['result']['balance']['balance']} DUCOs")
            print(Fore.YELLOW + "Total Transactions: "  + Style.RESET_ALL + f"{len(data['result']['transactions'])}")
            print(Fore.BLUE + "Total Miners: " + Style.RESET_ALL + f"{len(data['result']['miners'])}")
            print(Fore.MAGENTA + "Trust Score: " + Style.RESET_ALL + f"{data['result']['balance']['trust_score']}")
            print("---------------------------------------------------------------")
            
        time.sleep(tiempo)
        clear_screen()
        
if __name__ == "__main__":
    main()
