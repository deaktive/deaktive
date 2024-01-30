#!/usr/bin/env python3
import time, asyncio, sys, emoji


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'dexter'

Adv = '/boss103monster'
Suke = '/makanbuahiblis_DokuDokuNoMi'
Rain = 0
buff = 0

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('GrandPiratesBot', Adv))

    @client.on(events.NewMessage(from_users='GrandPiratesBot'))
    async def handler(event):
        global Rain
        global buff
        pesan = event.raw_text
        
        if 'Lawan BossBattle' in event.raw_text:
            Rain = 0
            time.sleep(1)
            await event.click(0,0)
            return
        
        if "Kamu memutuskan" in pesan:
            Rain += 1
            buff += 1
            if Rain > 2:
               time.sleep(1)
               await event.respond('/use_RainPowder')
               return
            if buff > 29:
               time.sleep(1)
               await event.respond('/use_Shusui_10')
               return
            else:
               print(time.asctime())
               time.sleep(1)
               await event.click(0,0)
               return
            return
            
        #if "Kalian saling beradu" in pesan:
            buff += 1
            if buff > 24:
               time.sleep(1)
               await event.respond('/use_Yubashiri_10')
               return
            else:
               print(time.asctime())
               time.sleep(1)
               await event.click(0,0)
               return
            return
        
        if 'Shusui 10x' in event.raw_text:
            buff = 0
            time.sleep(1)
            await event.respond(Suke)
            return
        
        if '10% energi dipulihkan' in event.raw_text:
            time.sleep(1)
            await event.respond(Suke)
            return
        
        if 'Berhasil memakan' in event.raw_text:
            time.sleep(1)
            await event.respond(Adv)
            return
        
        if 'Kamu hanya bisa' in event.raw_text:
            time.sleep(1)
            await event.respond(Adv)
            return
        
        if 'Kamu sudah menggunakan' in pesan:
            sft = pesan.find('dalam') + 5
            lsf = pesan.find('detik', sft) - 1
            tms = int(pesan[sft:lsf])
            print('tunggu : ', tms, ' detik')
            time.sleep(tms)
            await event.respond('/use_RainPowder')
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	