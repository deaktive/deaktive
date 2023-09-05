#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 19691895 
api_hash = 'c58b4f1b0b521f77b9378838ce3e6712'
sesi_file = 'arlen'

bot_id = 'KampungMaifamxBot'
Area = 'Hutan Sakral'
Alat = 'Tangkap'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text

            if "Kamu berhasil" in pesan:
                time.sleep(2)
                await event.respond(Area)
                return

            elif "Kamu masuk" in pesan:
                time.sleep(2)
                await event.respond(Alat)
                return

            elif "Kamu berusaha" in pesan:
                time.sleep(2)
                await event.respond(Area)
                return

            elif "Kamu berburu" in pesan:
                time.sleep(2)
                await event.respond(Alat)
                return    
                
            elif 'Kamu tidak memiliki' in pesan:
                time.sleep(2)
                await event.respond('/restore_max_confirm')
                print(time.asctime(), 'Isi Ulang Energi Dulu')
                return
                
            elif 'Energi berhasil' in pesan:
                time.sleep(2)
                await event.respond(Area)
                return
            
            elif 'Dalam perbaikan' in pesan:
                time.sleep(2)
                await event.respond('/makan_rotibelanda')
                return
            
            elif "kamu tidak bisa makan" in pesan:
                time.sleep(2)
                await event.respond(Area)
                return
        
            elif "Uuuh rasanya enak sekali" in pesan:
                time.sleep(2)
                await event.respond(Area)
                return
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
