#!/usr/bin/env python3
import time, asyncio, sys, emoji


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'dexter'

Adv = 'Adventure'
Suke = '/makanbuahiblis_SukeSukeNoMi'
df_suke = 0

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('GrandPiratesBot', Adv))

    @client.on(events.NewMessage(from_users='GrandPiratesBot'))
    async def handler(event):
        global df_suke
        
        if 'Kalahkan musuh' in event.raw_text:
            time.sleep(1)
            await event.click(text='Player Battle')
            return
        
        if 'Total Bounty' in event.raw_text:
            time.sleep(1)
            await event.click(text='Lawan') 
            return
        
        if 'Kamu memutuskan' in event.raw_text:
            df_suke += 1
            if df_suke > 20:
               time.sleep(1)
               await event.respond('/makanbuahiblis_SukeSukeNoMi')
               return
            else:
               time.sleep(1)
               await event.click(0,0)
               return
            return
        
        if 'Player Battle' in event.raw_text:
            time.sleep(1)
            await event.click(text='🏴‍☠️ TopiSayaBundar ')
            return
        
        if 'Berhasil memakan' in event.raw_text:
            df_suke = 0
            time.sleep(1)
            await event.respond(Adv)
            return
        
        if 'Kamu masih memiliki' in event.raw_text:
            df_suke = 0
            time.sleep(1)
            await event.respond(Adv)
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	