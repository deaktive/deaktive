import time, asyncio, sys, random
from telethon import TelegramClient, events, utils, Button

api_id = 8148872 
api_hash = 'e8008d73edd29d1a1600bf992712c089'

bot_id = 'KampungMaifamxBot'
sesi = input("Sesi: ")
print("Gudang?")

typ = input("Angka: ")

with TelegramClient(sesi, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, "/xm2023_GudangSanta_" + str(typ)))
        @client.on(events.NewMessage(from_users=bot_id))
          
        async def handler(event):
            pesan = event.raw_text
            
            if "Hadiah akan direset" in pesan:
                time.sleep(8)
                await event.click(0,0)
                return
            
            if "Kamu berusaha" in pesan:
                time.sleep(8)
                await event.click(0,0)
                return
            
            if "Pelan-pelan" in pesan:
                time.sleep(8)
                await event.click(0,0)
                return
            
            if "dari jauh melihat" in pesan:
                time.sleep(6)
                await event.click(0,0)
                return
            
            if "Kamu mencuri dari" in pesan:
                time.sleep(6)
                await client.send_message("mailogs", pesan)
                await event.click(0,0)
                return
            
            if "Berhasil mengambil" in pesan or "Pelan-pelan" in pesan:
                time.sleep(8)
                await event.click(text="Cari Hadiah")
                return

            if "iPong15ProMag" in pesan or "BonekaBeruang" in pesan or "Ransel" in pesan or "KaosKaki" or "GaunPrincess" in pesan or "XS5" in pesan or "Piyama" in pesan:
                time.sleep(8)
                await event.click(text="Ambil")
                return
            
client.start()
client.run_until_disconnected()        
