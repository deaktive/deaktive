#!/usr/bin/env python3
import time, asyncio, sys
from time import sleep


from telethon import TelegramClient, events, utils, Button

api_id = 1998603 
api_hash = '341eb9d72c2de53ef2e70269728d5fca'
sesi_file = 'puputfairy'

Mese = '/labsihir_Explosimorphis_100'
magi = '/kirimKeLab_magistone_1e6_confirm'
kali525 = '/kirimKeLab_Kalifornium525_5e5_confirm'
kali545 = '/kirimKeLab_Kalifornium545_5e5_confirm'
kali565 = '/kirimKeLab_Kalifornium565_5e5_confirm'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamxBot', Mese))

    @client.on(events.NewMessage(from_users='KampungMaifamxBot'))
    async def handler(event):

        if 'Berhasil membuat' in event.raw_text:
            time.sleep(2)
            await event.respond(Mese)
            return
        
        if 'Kamu tidak memiliki' in event.raw_text:
            time.sleep(2)
            await event.respond('/restore')
            return
        
        if 'Bahan tidak' in event.raw_text:
            time.sleep(2)
            await event.respond(magi)
            return
        
        if 'Magistone' in event.raw_text:
            time.sleep(2)
            await event.respond(kali525)
            return
        
        if 'Kalifornium525' in event.raw_text:
            time.sleep(2)
            await event.respond(kali565)
            return
        
        if 'Kalifornium565' in event.raw_text:
            time.sleep(2)
            await event.respond(kali545)
            return
        
        if 'Kalifornium545' in event.raw_text:
            time.sleep(2)
            await event.respond("/act_FullMagicAlchemist")
            return
        
        if 'FullMagicAlchemist' in event.raw_text:
            time.sleep(2)
            await event.click(text="Claim")
            await event.respond(Mese)
            print(time.asctime(), 'Cek Aktivitas Dulu!!!')
            return
        
        if 'Berhasil menyelesaikan' in event.raw_text:
            time.sleep(2)
            await event.respond(Mese)
            print(event.raw_text)
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	