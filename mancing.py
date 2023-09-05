#by Aditz
#!/usr/bin/env python3
import time
import asyncio
import sys, re

from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 19426024 
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = 'dexter'
loop = asyncio.new_event_loop()

#bot
print("\nPilih bot yng digunakan")
print("Contoh: Angka = 2")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n\tKetik 4 untuk Bot X5\n   Angka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'
elif mpm == '4':
    bot_id = 'KampungMaifamX5Bot'
    
#tempat mancing
print("\nPilih tempat mancing")
pilih = input('\tKetik 1 untuk 💦 Lala\n\tKetik 2 untuk 💦 Mimi\n\tKetik 3 untuk 💦 Badabu\n\tKetik 4 untuk 🏝 Soprano\n\tKetik 5 untuk 💧 Bulari\n\tKetik 6 untuk 🌊 Narrow/Sempit\n\tKetik 7 untuk 🌊 Gabagaba\n\tKetik 8 untuk 🌊 Ancient/Purba\n\tKetik 9 untuk 🌊 Haunted/Berhantu\n\tKetik 10 untuk 🌊 All\n\tKetik 11 untuk 💦 Danau Penjara\n   Angka =  ')
if pilih == '1': 
    tempat = 'Lala River' 
elif pilih == '2': 
    tempat = 'Mimi River' 
elif pilih == '3': 
    tempat = 'Badabu River' 
elif pilih == '4': 
    tempat = 'Soprano Lake' 
elif pilih == '5': 
    tempat = 'Bay of Bulari' 
elif pilih == '6': 
    tempat = 'Narrow Sea'
elif pilih == '7': 
    tempat = 'Gabagaba Ocean' 
elif pilih == '8': 
    tempat = 'Ancient Sea' 
elif pilih == '9': 
    tempat = 'Haunted Sea'
elif pilih == '10': 
    tempat = 'All Sea'
elif pilih == '11': 
    tempat = 'Danau Penjara'
    
#alat pancing
print("\nPilih jenis alat")
pilih = input('\tKetik 1 untuk 🎣 Pancing\n\tKetik 2 untuk 🎣 Rod\n\tKetik 3 untuk 🕸 Jala\n\tKetik 4 untuk 🕸 Net\n   Angka = ')
if pilih == '1': 
    alat = 'Tarik Alat Pancing' 
elif pilih == '2': 
    alat = 'Pull The Fishing Rod' 
elif pilih == '3': 
    alat = 'Tarik Jala' 
elif pilih == '4': 
    alat = 'Pull The Net' 
    
#narasi di bot
lala1 = "Doesn't look like"
lala2 = "Sungai dangkal"
mimi1 = "Legend said a man"
mimi2 = "Legenda mengatakan"
badabu1 = "Only big fish"
badabu2 = "Hanya ikan besar"
soprano1 = "Rare fish lived"
soprano2 = "Ikan langka"
bulari1 = "Well, some little"
bulari2 = "Terletak di bagian"
narrow1 = "People claimed that"
narrow2 = "Orang-orang mengklaim"
gaba1 = "Many years ago"
gaba2 = "Bertahun-tahun yang"
ancient1 = "A dangerous strange"
ancient2 = "Laut aneh berbahaya"
haunted1 = "A cursed sea"
haunted2 = "Laut terkutuk"
all1 = "Here you can"
all2 = "Bagian kecil"
penjara1 = "The Government"
penjara2 = "Pemerintah Maikantri"
        
tunggu = 2
       
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tempat))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
                   
        if lala1 in pesan or lala2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
                     
        if mimi1 in pesan or mimi2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
            
        if badabu1 in pesan or badabu2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
                   
        if soprano1 in pesan or soprano2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
        
        if bulari1 in pesan or bulari2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
                    
        if narrow1 in pesan or narrow2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
                    
        if gaba1 in pesan or gaba2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return        
            
        if ancient1 in pesan or ancient2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return      
                     
        if haunted1 in pesan or haunted2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
        
        if all1 in pesan or all2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
        
        if penjara1 in pesan or penjara2 in pesan:
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return
        
        if "You've got" in pesan or "Kamu mendapatkan" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "You've caught" in pesan or "berhasil menangkap" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "not fishing" in pesan or "tidak sedang memancing" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "Your energy is" in pesan or 'Kamu tidak memiliki' in pesan:
            time.sleep(tunggu)
            await event.respond("/restore_max_confirm")
            return
        
        if "Energy Successfully" in pesan or 'Energi berhasil' in pesan:
            time.sleep(tunggu)
            await event.respond("/eat_rotibelanda")
            return
        
        if "kamu tidak bisa makan" in pesan:
            print('Makan Dulu Banh')
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "Uuuh rasanya enak sekali" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
client.start()
print()
print(time.asctime(), '-', 'Lesgoo mancing 🎣')
client.run_until_disconnected()
print(time.asctime(), '-', 'Lelah ges')