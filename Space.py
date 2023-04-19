import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dextervps'

bot_id = 'KampungMaifamxBot'
Mine = '⛏'
mese = 'SpaceExploration'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, mese))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "Proses tambang "  in pesan:
                time.sleep(270)
                await event.click(text=Mine)                
                print(time.asctime(), 'Tambang')
                return

            if "SpaceMiner"  in pesan:
                time.sleep(2)
                await event.respond('/spaceExploration')                
                print(time.asctime(), 'Menu')
                return
          
            if "Chrysus"  in pesan:
                time.sleep(2)
                await event.click(text=Mine)                
                print(time.asctime(), 'Tambang')
                return

            if "Tunggu sekitar"  in pesan:
                time.sleep(30)
                await event.click(text=mine)                
                print(time.asctime(), 'Menu')
                return

client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
