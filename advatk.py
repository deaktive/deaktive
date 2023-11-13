import time, asyncio, sys, random
import logging
from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = "dexterop"

bot_id = 'GrandPiratesBot'
adv = '/adventure'
buff = '/use_Shigure_10'
upkapal = '/levelupKapal_ATK'
kapal = '/levelupKapal'
buah = '/makanbuahiblis_SukeSukeNoMi'
exp_pil = 0


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
            
            if "sudah mencapai batas maksimal" in pesan:
                tunggu_hingga_menit_detik_00()
                await event.respond('/adventure')
                return
            
            if "Arus laut" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            if "oleh 4 musuh:" in pesan:
               time.sleep(1)
               await event.click(0,0)
               return
        
            if "oleh 3 musuh:" in pesan:
               time.sleep(1)
               await event.click(0,0)
               return
        
            if "oleh 2 musuh:" in pesan:
               time.sleep(1)
               await event.click(1,0)
               return
        
            if "oleh 1 musuh:" in pesan:
               time.sleep(1)
               await event.click(1,0)
               return
           
           if "mengalahkan" in pesan:
               time.sleep(2)
               await event.click(1,0)
               return
            
            if "KAMU MENANG!!" in pesan:
                buff += 1
                if buff > 25:
                   time.sleep(2)
                   await event.respond('/use_Shigure_10')
                   return
                else:
                   print(time.asctime())
                   time.sleep(1)
                   await event.click(0,0)
                   return
                return
            
            if "Berhasil menggunakan" in pesan:
                buff = 0 
                time.sleep(2)
                await event.respond(kapal)
                return
            
            if "Musuh menang..." in pesan:
                time.sleep(2)
                await event.respond('/use_Shigure_10')
                return
            
            if "Kamu masih" in pesan:
                time.sleep(2)
                await event.respond('/levelupKapal')  
                return
            
            if "Kamu hanya" in pesan:
                time.sleep(2)
                await event.respond('/levelupKapal')  
                return
            
            if "Silakan pilih" in pesan:
                time.sleep(2)
                await event.respond('/levelupKapal_ATK')  
                return
            
            if "saat naik" in pesan:
                time.sleep(2)
                await event.click(0,0)  
                return
            
            if "Berhasil meningkatkan" in pesan:
                time.sleep(2)
                await event.respond('/adventure')  
                return
            
            if "Kapalmu masih" in pesan:
                time.sleep(2)
                await event.respond('/adventure')  
                #await event.respond('/restore_x')  
                return
                
            if "Berhasil memulihkan" in pesan:
                time.sleep(2)
                await event.respond('/adventure')
                return
            
            
client.start()
print('Started')
client.run_until_disconnected()