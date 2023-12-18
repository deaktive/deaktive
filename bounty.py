#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'dexter'

Adv = 'Adventure'
Nama = '🏴‍☠ Mordekaiser'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('GrandPiratesBot', Adv))

    @client.on(events.NewMessage(from_users='GrandPiratesBot'))
    async def handler(event):
        
        if 'Kalahkan musuh' in event.raw_text:
            time.sleep(2)
            await event.click(text='Player Battle')
            return
        
        if 'Total Bounty' in event.raw_text:
            time.sleep(2)
            await event.click(text='Lawan') 
            return
        
        if 'Kamu memutuskan' in event.raw_text:
            time.sleep(1.5)
            await event.click(0,0) 
            return
        
        if 'Player Battle' in event.raw_text:
            time.sleep(1.5)
            await event.click(text='🏴‍☠ Mordekaiser')
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	