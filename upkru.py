#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'arlen'

Adv = 'DaftarKru'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('GrandPiratesBot', Adv))

    @client.on(events.NewMessage(from_users='GrandPiratesBot'))
    async def handler(event):
        
        if 'Tingkatkan lagi' in event.raw_text:
            time.sleep(1)
            await event.click(0,0)
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	