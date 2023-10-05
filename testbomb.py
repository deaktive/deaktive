#!/usr/bin/env python3
import time, asyncio, sys
from time import sleep


from telethon import TelegramClient, events, utils, Button

api_id = 1998603 
api_hash = '341eb9d72c2de53ef2e70269728d5fca'
sesi_file = 'puputfairy'

Mese = '💣'
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamxBot', Mese))

    @client.on(events.NewMessage(from_users='KampungMaifamxBot'))
    async def handler(event):
        global tmp

        if 'Bomb meledak' in event.raw_text:
            time.sleep(2)
            await event.respond('/act_TheArchaeologist')
            return
        
        if 'TheArchaeologist' in event.raw_text:
            time.sleep(2)
            await event.click(text="Claim")
            await event.respond('/act_GoldDigger')
            print(time.asctime(), 'Cek Aktivitas Dulu!!!')
            return
        
        if 'GoldDigger' in event.raw_text:
            time.sleep(2)
            await event.click(text="Claim")
            await event.respond(Mese)
            print(time.asctime(), 'Cek Aktivitas Dulu!!!')
            return
        
        if 'Berhasil menyelesaikan' in event.raw_text:
            time.sleep(2)
            await event.respond(Mese)
            print(event.raw_text)
            return
        
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	