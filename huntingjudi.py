#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'puputfairy'

bot_id = 'KampungMaifamBot'
Area = 'Hutan 4'
Alat = 'Tangkap'
Casino = '/casino_UltraLuck_25_5e9'
cek_act = 0

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            global cek_act

            if "Kamu berhasil" in pesan:
                cek_act += 1
                if cek_act > 20:
                    time.sleep(2)
                    await event.respond("/act_DragonSlayer")
                    return
                else:
                    print('Casino')
                    time.sleep(2)
                    await event.respond('/casino_hasil')
                    return
                return

            if "CatatanAktivitas" in pesan:
                cek_act = 0
                time.sleep(2)
                await event.click(text="Claim")
                time.sleep(2)
                await event.respond(Area)
                print ('Cek Act')
                return
 
            if "BayiNaga" in pesan or "NagaPutih" in pesan or "NagaHitam" in pesan:
                time.sleep(2)
                print('Dapet Naga')
                await event.respond(Alat)
                return

            elif "Kamu berusaha" in pesan:
                time.sleep(2)
                await event.respond(Area)
                print(pesan)
                return

            elif "Kamu berburu" in pesan:
                time.sleep(2)
                await event.respond(Alat)
                return 
            
            elif "Kamu bertaruh untuk angka" in pesan:
                time.sleep(2)
                await event.respond("/casino_UltraLuck_"+str(random.randint(1,50))+"_5e9") 
                return

            elif "Berhasil bertaruh" in pesan:
                time.sleep(2)
                await event.respond(Area) 
                return

            elif "Selesaikan permainan sebelumnya" in pesan:
                time.sleep(2)
                await event.respond(Area)
                return

            elif "Belum ada taruhan" in pesan:
                time.sleep(2)
                await event.respond(Casino)
                return

            elif "Hasil akan keluar" in pesan:
                time.sleep(2)
                await event.respond(Area)
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
            
            elif 'Berhasil menyelesaikan' in event.raw_text:
                time.sleep(2)
                await event.respond(Area)
                print('Klaim Act')
                return
            
            else:
                time.sleep(2)
                await event.respond(Area)
                return
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')