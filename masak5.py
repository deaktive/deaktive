#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'kael1'

Casino = '/masak_MiniBacon_220'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamBot', Casino))

    @client.on(events.NewMessage(from_users='KampungMaifamBot'))
    async def handler(event):
        
        if 'Berhasil memasak' in event.raw_text:
            time.sleep(2)
            await event.respond('/masak_MiniBacon_220')
            return
        
        if 'Kamu tidak memiliki' in event.raw_text:
            time.sleep(2)
            await event.respond('/restore')
            return
        
        if 'Energi berhasil' in event.raw_text:
            time.sleep(2)
            await event.respond(Casino)
            return
        
        if 'Kamu tidak bisa memasak' in event.raw_text:
            time.sleep(1200)
            await event.respond(Casino)
            return
        
        if 'Tidak cukup bahan' in event.raw_text:
            time.sleep(2)
            await event.respond('/dapur_restock_MAX_confirm')
            print(time.asctime(), 'Bahan Gak Cukup')
            return
        
        if 'Bahan-bahan direstock' in event.raw_text:
            time.sleep(2)
            await event.respond(Casino)
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	