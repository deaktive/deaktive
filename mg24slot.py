import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'arlen'

bot_id = 'KampungMaifamBot'
Mine = '⛏⛏⛏'
mese = '/mg24'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, mese))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text

            if "Poin didapat"  in pesan:
                time.sleep(4.5)
                await event.click(0,0)                
                return

            if "Kamu memutar"  in pesan:
                time.sleep(4.5)
                await event.click(0,0)             
                return

            if "Tunggu sekitar"  in pesan:
                time.sleep(31)
                await event.click(text=Mine)                
                print(time.asctime(), 'Tambang')
                return

client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
