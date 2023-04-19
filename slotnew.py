import time, asyncio, sys, random

from telethon import TelegramClient, events, utils, Button

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dexter'

cmd = '/th_SlotMachine_SevenFish'
cmd1 = '/th_SlotMachine_add'
bot = 'KampungMaifamXBot'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot, cmd))
        @client.on(events.NewMessage(from_users=bot))
        async def handler(event):
            
            if '1000000Qn' in event.raw_text:
                time.sleep(2)
                await event.respond('/tamanHiburan_TembakTopeng')
                print('Mulai Dart')
                return
#350000
            elif 'Ada tujuh' in event.raw_text:
                time.sleep(2)
                await event.click(text="Play 10x (Bonus 1)")
                return
            
            elif 'Kamu memutar SlotMachine' in event.raw_text:
                time.sleep(2)
                await event.click(1,0)
                return
            
            elif 'Kamu memerlukan' in event.raw_text:
                time.sleep(2)
                await event.click(text="Play")
                return
            
            elif 'Kamu memutar SlotMachine 10x' in event.raw_text:
                time.sleep(2)
                await event.respond(cmd1)
                return
            
            elif 'Koin untuk' in event.raw_text:
                time.sleep(2)
                await event.respond(cmd1)
                return
            
            elif 'Apa kamu' in event.raw_text:
                time.sleep(2)
                await event.click(text="Confirm")
                return
            
            elif 'Berhasil membeli' in event.raw_text:
                time.sleep(2)
                await event.respond(cmd)
                return
            
            elif 'Setiap harinya' in event.raw_text:
                time.sleep(2)
                await event.click(text='Mulai')
                return
 
            elif 'Pilih sasaran' in event.raw_text:
                time.sleep(2)
                await event.click(0,1)
                return
            
            elif 'Lemparanmu berhasil' in event.raw_text:
                time.sleep(2)
                await event.click(text='Lanjut')
                return
            
            elif 'Sayang sekali' in event.raw_text:
                time.sleep(2)
                await event.click(text='Lanjut')
                return

            elif 'Kesempatan' in event.raw_text:
                time.sleep(2)
                print('--Selesai--')
                exit


        client.start() 
        client.run_until_disconnected() 
        print(time.asctime(), '-', 'berhenti')
	
