#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 19088515 
api_hash = 'a414cdd5cacd7f93ec0b992b57802458'
sesi_file = 'celipso'

Casino = '/beriMakan'
Masak = '/masak_minibacon_220'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamBot', Casino))

    @client.on(events.NewMessage(from_users='KampungMaifamBot'))
    async def handler(event):
        if 'Berhasil memberi' in event.raw_text:
            time.sleep(2)
            await event.respond('/ambilHasil')
            return
        
        if 'Kamu memperoleh' in event.raw_text:
            time.sleep(2)
            await event.respond('/beriMakan')
            return
        
        if 'Kamu tidak memiliki' in event.raw_text:
            time.sleep(2)
            await event.respond('/restore')
            return
        
        if 'Energi berhasil' in event.raw_text:
            time.sleep(2)
            await event.respond(Masak)
            return
        
        if 'Tak ada ternak' in event.raw_text:
            time.sleep(2)
            await event.respond('/ambilHasil')
            return
        
        if 'Berhasil memasak' in event.raw_text:
            time.sleep(2)
            await event.respond('/masak_minibacon_220')
            return
        
        if 'Kamu tidak bisa memasak' in event.raw_text:
            time.sleep(2)
            await event.respond('/beriMakan')
            return
        
        if 'Tidak cukup bahan' in event.raw_text:
            time.sleep(2)
            await event.respond('/dapur_restock_MAX_confirm')
            print(time.asctime(), 'Bahan Gak Cukup')
            return
        
        if 'Bahan-bahan direstock' in event.raw_text:
            time.sleep(2)
            await event.respond(Masak)
            return
        
        if 'Tidak ada hasil' in event.raw_text:
            time.sleep(2)
            await event.respond('/beriMakan')
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	