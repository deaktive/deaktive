import time
import asyncio
import sys
import re
import threading
from telethon import TelegramClient, events, utils

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'

mepam = 'kampungmaifambot'
mepam2 = 'kampungmaifambot'

punyaku = [ 
"dexter",
"puputfairy",
"Arlen",
"aegon",
"havertz",
"daeron",
"rektharrow",
"daemond",
"kirby",
"tywin",
"jorah",
"arryn",
"joffrey",
"arryk",
"serharwin",
"corlys",
"laenor",
"larys",
"jacaerys",
"lucerys",
"otto",
"serharrold",
"raegan",
"raizen",
"rouvin",
"rycluse",
"chung",
"boyce",
"ppt1",
"ppt2",
"ppt3",
"ppt4",
"ppt5",
"ppt6",
"ppt7",
"ppt8",
]

cmd = [
'/pd2023_claim_50',
'/pd2023_claim_75',
'/pd2023_claim_125',
'/pd2023_claim_150',
'/pd2023_claim_200',
'/pd2023_claim_250',

'Last',
]

ulang = [
'',
'Last',
]

mer = 0
ger = 0

alamat = '/pd2023_claim_25'

while True:
    for aaa in punyaku:
        with TelegramClient(aaa, api_id, api_hash) as client:
            client.loop.run_until_complete(client.send_message(mepam, alamat))
            @client.on(events.NewMessage(from_users=mepam))
            async def handler(event):
                global mer
                global idMer
                global ger
                print(event.text)
                
                #if 'Tiap kali' in event.raw_text:
                    #time.sleep(2)
                    #await client.forward_messages('link',  event.message)
                    #await client.disconnect()
                    #close()
                    
#                if 'Selamat Hari Buruh' in event.raw_text:
#                    time.sleep(2)
#                    await event.click(0,0)
#                    return
                    
                if 'Kumpulkan' in event.raw_text:
                    mer += 0
                    time.sleep(2)
                    await client.disconnect()
                    print("Klaim")
                    return
                
                if 'Berhasil mengklaim' in event.raw_text:
                    mer += 1
                    time.sleep(2)
                    await event.respond(''+cmd[mer])
                    return
                
                if 'Bonus sudah' in event.raw_text:
                    mer += 1
                    time.sleep(2)
                    await event.respond(''+cmd[mer])
                    return
                
                if cmd[mer] == cmd[-1]:
                    ger +=0
                    mer = 0
                    print('Selesai Semua')
                    time.sleep(2)
                    await client.disconnect()
                    return
            
                if ulang[ger] == ulang[-1]:
                    ger = 0
                    mer = 0
                    print('Diulang')
                    time.sleep(2)
                    await client.disconnect()
                    close()
                    
            client.run_until_disconnected()
        print(aaa, 'selesai setor alamat', time.asctime())
    client.run_until_disconnected()
time.sleep(1800)
