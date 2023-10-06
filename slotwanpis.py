#!/usr/bin/env python3
import time, asyncio, sys

from telethon import TelegramClient, events, utils

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dexter'

#Slot apa
print("\nPilih mau slot apa?")
pilih = input('\tKetik 1 untuk 💰 BigChance\n\tKetik 2 untuk 💎 RainDinner\n   Angka =  ')
if pilih == '1': 
    Slot = '/visit_BigChance' 
elif pilih == '2': 
    Slot = '/visit_Raindinners'

#CoinBerapa
print("\nPilih mau coin berapa")
pilih = input('\tKetik 1 untuk 🪙\n\tKetik 2 untuk 🪙🪙\n\tKetik 3 untuk 🪙🪙🪙\n\tKetik 4 untuk 💎\n    Angka =  ')
if pilih == '1': 
    Coin = '🪙'
elif pilih == '2': 
    Coin = '🪙🪙'
elif pilih == '3': 
    Coin = '🪙🪙🪙'
elif pilih == '4': 
    Coin = 'Play (-1💎)'
    
#hadiah

SmallBeers = 0
GiantBeer = 0 
DeluxeWine = 0 

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('GrandPiratesBot', Slot))

    @client.on(events.NewMessage(from_users='GrandPiratesBot'))
    async def handler(event):
        global SmallBeers
        global GiantBeer
        global DeluxeWine
        
        if 'Tempat judi terbesar' in event.raw_text:
            time.sleep(2)
            await event.click(text=Coin)
            return
        
        if 'Tidak banyak hadiah' in event.raw_text:
            time.sleep(3)
            await event.click(text=Coin)
            return
        
        if 'koin dilempar' in event.raw_text:
            time.sleep(3)
            await event.click(text=Coin)
            return
        
        if 'Kamu memutar slot' in event.raw_text:
            time.sleep(2)
            await event.click(0,0) 
            return
        
        if '🍻 SmallBeers' in event.raw_text:
            time.sleep(2)
            SmallBeers+=1
            print(SmallBeers)
            return
        
        if '🍺 GiantBeer' in event.raw_text:
            time.sleep(2)
            GiantBeer+=1
            print(GiantBeer)
            return
        
        if '🍷 DeluxeWine' in event.raw_text:
            time.sleep(2)
            DeluxeWine+=1
            print(DeluxeWine)
            return
        
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	