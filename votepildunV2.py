import time
import asyncio
import sys
import re
import threading
from telethon import TelegramClient, events, utils

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'

mepam = 'kampungmaifamxbot'

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
]

#punyaku = ['ipenaja']

negara = input ("Negara apa = ")
b = "/pd2023_pilih_"
cmd = b+negara

def cekcode(pesan):
    f1 = "jagokan:"
    f = pesan.find(f1) + len(f1)
    l = pesan.find("Tulis", f) - 2
    code = pesan[f:l]
    # print(code)
    kode = [
        [1, "satu"], 
        [2, "dua"], 
        [3, "tiga"], 
        [4, "empat"], 
        [5, "lima"], 
        [6, "enam"], 
        [7, "tujuh"], 
        [8, "delapan"], 
        [9, "sembilan"], 
        [0, "nol"]
        ]
    
    code = code.replace("*", "")
    p = code.split()
    # p[0] = p[0][2:len(p[0])]
    print(p)
    angka = ""
    for i in p:
        t = False
        for j in range(len(kode)):
            if i == kode[j][1]:
                angka += str(kode[j][0])
                t = True
                break

            if not t:
                tels = kode[j][1]
                lee = len(tels)
                for k in range(lee-2):
                    sub = tels[:k] + tels[k+1:]
                    if i == sub:
                        angka += str(kode[j][0])
                        t = True
                        break

            if not t:
                tels = kode[j][1]
                lee = len(tels)
                m = lee-1
                for k in range(lee-2):
                    subs = ""
                    for l in range(lee):
                        # sub = tels[:k] + tels[l+1:]
                        if not (l == k or l == m) :
                            subs += tels[l]
                        # print(subs)
                    m -= 1
                    if i == subs:
                        angka += str(kode[j][0])
                        t = True
                        break

    # print(angka)
    return angka

while True:
    for aaa in punyaku:
        with TelegramClient(aaa, api_id, api_hash) as client:
            client.loop.run_until_complete(client.send_message(mepam, cmd))
            @client.on(events.NewMessage(from_users=mepam))
            async def handler(event):
                global mer
                global idMer
                global ger
                pesan = event.text
                    
                if 'Untuk memilih tim' in pesan:
                    time.sleep(2)
                    await event.respond('/pd2023_kode')
                    return
                
                if 'Gunakan kode' in pesan:
                    kode = cekcode(pesan)
                    pildun = cmd+'_'+kode
                    print('cmd pildun : ', pildun)
                    time.sleep(2)
                    await event.respond(pildun)
                    return
                
                if 'Kode salah' in pesan:
                    time.sleep(2)
                    await event.respond('/pd2023_kode')
                    return
                
                if 'Apa kamu yakin' in pesan:
                    time.sleep(2)
                    await event.click(0,0)
                    return
                
                if 'mendukung timnas' in pesan:
                    time.sleep(2)
                    await client.disconnect()
                    # close()
                    
            client.run_until_disconnected()
        print(aaa, 'selesai setor alamat', time.asctime())
    client.run_until_disconnected()
time.sleep(1800)
