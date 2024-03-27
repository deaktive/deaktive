import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'daeron'

bot_id = 'KampungMaifamBot'
Mine = '⛏⛏⛏'
mese = '/mg24_game_Tambahan_70'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, mese))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text

            if "Kumpulkan poin"  in pesan:
                time.sleep(1.5)
                await event.click(0,0)                
                print(time.asctime(), 'Tambang')
                return
            
            if "Apa kamu yakin"  in pesan:
                time.sleep(1.5)
                await event.click(0,0)                
                return
            
            if "Permainan dimulai"  in pesan:
                time.sleep(1.5)
                await event.respond('/mg24')                
                return

            if "Kamu menambang"  in pesan:
                time.sleep(24)
                await event.click(text=Mine)             
                print(time.asctime(), 'Tambang')
                return

client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
