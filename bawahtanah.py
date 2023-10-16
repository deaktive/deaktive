#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dexter'

bot_id = 'KampungMaifamxBot'
Area = 'Gua Bawah Tanah'
Alat = '⛏'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text

            if "GuaBawahTanah" in pesan:
                time.sleep(2)
                await event.click(text=Alat)
                print(pesan)
                return

            elif "Kamu mendapat" in pesan:
                time.sleep(2)
                await event.click(text=Alat)
                print(pesan)
                return
                
            elif 'Kamu tidak memiliki' in pesan:
                time.sleep(2)
                await event.respond('/restore_max_confirm')
                print(time.asctime(), 'Isi Ulang Energi')
                return
                
            elif 'Energi berhasil' in pesan:
                time.sleep(2)
                await event.respond(Area) 
                return
            
            else :
                time.sleep(2)
                await event.click(text=Alat)
                print(time.asctime(), 'Lempar bom')
                print(pesan)
                return
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')