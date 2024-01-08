import time, asyncio, sys, random
import logging
from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = "dexterop"

bot_id = 'GrandPiratesBot'
adv = '/visit_TorinoTree_NanasGrandline'

logging.basicConfig(level=logging.ERROR)

def tunggu_hingga_menit_detik_00():
    saat_ini = time.localtime()
    menit_sekarang = saat_ini.tm_min
    detik_sekarang = saat_ini.tm_sec
    
    if menit_sekarang == 0 and detik_sekarang == 0:
        return  # Sudah 00:00, tidak perlu menunggu
    
    detik_yang_harus_ditunggu = (60 - menit_sekarang) * 60 - detik_sekarang
    print(f"Menunggu hingga 00:00.")
    time.sleep(detik_yang_harus_ditunggu)


with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, adv))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            global buff
            
            if "tidak sedang lapar" in pesan:
                tunggu_hingga_menit_detik_00()
                await event.respond('/visit_TorinoTree_NanasGrandline')
                return
            
            if "Berhasil memberi makan" in pesan:
                time.sleep(2)
                await event.respond('/visit_TorinoTree')
                return
            
            if "Beri makan menggunakan" in pesan:
               time.sleep(2)
               await event.respond('/visit_TorinoTree_NanasGrandline')
               return
            
client.start()
print('Started')
client.run_until_disconnected()