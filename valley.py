#!/usr/bin/env python3
import time, asyncio, sys, random

from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dexter'

bot_id = 'GrandPiratesBot'
Chat = '/bobValley'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id,Chat))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text

            if "Ratusan ribu" in pesan:
                time.sleep(20)
                await event.click(0,0)
                return
            
            if "(+100 Poin)" in pesan:
                time.sleep(20)
                await event.click(0,0)
                return
            
            if "(+400 Poin)" in pesan:
                time.sleep(20)
                
                return
            
            if "(+1000 Poin)" in pesan:
                time.sleep(20)
    
                return
            else:
                time.sleep(20)
                await event.click(0,0)
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')