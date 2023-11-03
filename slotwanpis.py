#!/usr/bin/env python3
import time, asyncio, sys

from telethon import TelegramClient, events, utils

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dexter'

#Slot apa
print("\nPilih mau slot apa?")
pilih = input('\tKetik 1 untuk 💰 BigChance\n\tKetik 2 untuk 💎 RainDinner\n\tKetik 3 untuk 🎫 GoldenCoupons\n  Angka =  ')
if pilih == '1': 
    Slot = '/visit_BigChance' 
elif pilih == '2': 
    Slot = '/visit_Raindinners'
elif pilih == '3':
    Slot = '/visit_GoldenCoupons'
ampas = 0

#CoinBerapa
print("\nPilih mau coin berapa")
pilih = input('\tKetik 1 untuk 🪙\n\tKetik 2 untuk 🪙🪙\n\tKetik 3 untuk 🪙🪙🪙\n\tKetik 4 untuk -1💎\n\tKetik 5 untuk -10💎\n\tKetik 6 untuk 🎫 BeliKupon\n\tKetik 7 untuk 🎟\n    Angka =  ')
if pilih == '1': 
    Coin = '🪙'
elif pilih == '2': 
    Coin = '🪙🪙'
elif pilih == '3': 
    Coin = '🪙🪙🪙'
elif pilih == '4': 
    Coin = 'Play (-1💎)'
elif pilih == '5': 
    Coin = 'Play (-10💎)'
elif pilih == '6':
    Coin = '/shop_GoldenCoupons_beli_20'
elif pilih == '7':
    Coin = 'Play (-1🎟)'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('GrandPiratesBot', Slot))

    @client.on(events.NewMessage(from_users='GrandPiratesBot'))
    async def handler(event):
        global ampas
        
        if 'Tempat judi terbesar' in event.raw_text:
            ampas = 0
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
        
        if 'memenangkan Hadiah' in event.raw_text:
            time.sleep(2)
            await event.click(text=Coin) 
            return
        
        if "lain kali" in event.raw_text:
            ampas += 1
            if ampas > 3:
                time.sleep(2)
                await event.respond(Slot)
                return
            else:
                print(time.asctime())
                time.sleep(1)
                await event.click(text=Coin)
                return
            return
        
        if 'Gedung judi' in event.raw_text:
            time.sleep(2)
            await event.respond(Coin) 
            return
        
        if 'Berhasil membeli' in event.raw_text:
            time.sleep(2)
            await event.respond(Coin) 
            return
        
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	