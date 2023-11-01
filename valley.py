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
            
            if "charle" in pesan:
                time.sleep(20)
                await event.respond('Bunuh charle')
                return
            
            if "lastar" in pesan:
                time.sleep(20)
                await event.respond('Bunuh lastar')
                return
            
            if "shawny" in pesan:
                time.sleep(20)
                await event.respond('Bunuh shawny')
                return
            
            if "edward" in pesan:
                time.sleep(20)
                await event.respond('Bunuh edward')
                return
            
            if "hendery" in pesan:
                time.sleep(20)
                await event.respond('Bunuh hendery')
                return
            
            if "gukguk" in pesan:
                time.sleep(20)
                await event.respond('Bunuh gukguk')
                return
            
            if "ganari" in pesan:
                time.sleep(20)
                await event.respond('Bunuh ganari')
                return
            
            if "brondo" in pesan:
                time.sleep(20)
                await event.respond('Bunuh brondo')
                return
            
            if "denver" in pesan:
                time.sleep(20)
                await event.respond('Bunuh denver')
                return
            
            if "prondous" in pesan:
                time.sleep(20)
                await event.respond('Bunuh prondous')
                return
            
            if "saori" in pesan:
                time.sleep(20)
                await event.respond('Bunuh saori')
                return
            
            if "rawon" in pesan:
                time.sleep(20)
                await event.respond('Bunuh rawon')
                return
            
            if "Ghobi" in pesan:
                time.sleep(20)
                await event.respond('Bunuh Ghobi')
                return
            
            if "arissa" in pesan:
                time.sleep(20)
                await event.respond('Bunuh arissa')
                return
            
            if "evelline" in pesan:
                time.sleep(20)
                await event.respond('Bunuh evelline')
                return
            
            if "Chroro" in pesan:
                time.sleep(20)
                await event.respond('Bunuh Chroro')
                return
            
            if "sebastian" in pesan:
                time.sleep(20)
                await event.respond('Bunuh sebastian')
                return
            
            if "geldo" in pesan:
                time.sleep(20)
                await event.respond('Bunuh geldo')
                return
            
            if "sopie" in pesan:
                time.sleep(20)
                await event.respond('Bunuh sopie')
                return
            
            if "alrena" in pesan:
                time.sleep(20)
                await event.respond('Bunuh alrena')
                return
            
            if "gilbert." in pesan:
                time.sleep(20)
                await event.respond('Bunuh gilbert')
                return
            
            if "sergio" in pesan:
                time.sleep(20)
                await event.respond('Bunuh sergio')
                return
            
            else:
                time.sleep(20)
                await event.click(0,0)
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')