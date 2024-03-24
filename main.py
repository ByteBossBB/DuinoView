"""
Name: Duino-Coin Data Viewer
Author: ByteBoss
Data Time: 24/03/2024
Description: This script displays a user's Duino-Coin account data., This script displays the data of a user's Duino-Coin account.
"""

import requests
import time
import os

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
            print("---------------------------------------------------------------")
            print(f"Username: {data['result']['balance']['username']}")
            print(f"Balance: {data['result']['balance']['balance']} DUCOs")
            print(f"Total Transactions: {len(data['result']['transactions'])}")
            print(f"Total Miners: {len(data['result']['miners'])}")
            print(f"Trust Score: {data['result']['balance']['trust_score']}")
            print("---------------------------------------------------------------")
            print("###############################################################")
            print("Transactions:")
            for i in range(len(data['result']['transactions'])):
                print("........................................................")
                print(f"Sender: {data['result']['transactions'][i]['sender']}")
                print(f"Amount: {data['result']['transactions'][i]['amount']}")
                print(f"Data Time: {data['result']['transactions'][i]['datetime']}")
                print(f"Memo: {data['result']['transactions'][i]['memo']}")
                print("........................................................")
            print("###############################################################")
            print("***************************************************************")
            print("Miners:")
            for i in range(len(data['result']['miners'])):
                print(f"Miner name: {data['result']['miners'][i]['identifier']}")
                print(f"Hashrate: {data['result']['miners'][i]['hashrate']}")
                print(f"Diff: {data['result']['miners'][i]['diff']}")
                print(f"Software: {data['result']['miners'][i]['software']}")
            print("***************************************************************")
        time.sleep(tiempo)
        clear_screen()
        
if __name__ == "__main__":
    main()
