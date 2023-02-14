from telethon import TelegramClient, events, sync, utils
from time import sleep
import asyncio

loop = asyncio.get_event_loop()

api_id = 15338487
api_hash = '018ea2f67c3a446cfe44ca5cfd5f49bb'
client = TelegramClient('aemond', api_id, api_hash).start()

total = 0
# tmp = 0
Masak = '/masak_minibacon_220'

chat = client.get_input_entity('kampungmaifamx4bot')
report = client.get_input_entity('housestolen')
testing = client.get_input_entity('anakbundy')
curiduit = False
curibarang = False

def hasilCurian(pesan):
    fnd = pesan.find('mencuri:') + len('mencuri:')
    lfnd = pesan.find('kemampuan', fnd) - 1
    text = pesan[fnd:lfnd]
    stext = text.split()

    data = []
    for i in stext:
        if len(i) > 3:
            data.append(i)

    print(data)

    ygdicari = ["⭐️WonderstoneOfYouth", "⭐️Stealestrite", "⭐️HyperstoneOfYouth"]
    found = False
    for i in data:
        for j in ygdicari:
            if i == j:
                found = True
                break

    return found
        

@client.on(events.NewMessage(chat))
async def handler(event):
    msg = event.raw_text
    global maling, curibarang, curiduit
    global total 
    global tmp
    

    if "Rumah Warga" in event.text:
        curibarang = True
        curiduit = False
        tmp = 0
        rem = 0
        maling = [x for x in event.text.split() if '/curiBarang' in x]
        sleep(2)
        await event.respond(maling[tmp])
        return
        
    if "Kamu berhasil mencuri" in event.raw_text and curibarang:
        sleep(2)
        tmp +=1
        # print(event.raw_text)
        ygdicari = hasilCurian(event.raw_text)

        if ygdicari:
            sleep(2)
            #await client.send_message(testing, event.raw_text)
            await client.send_message(report, event.raw_text)
        
        if tmp == 10:
            await event.respond("4")
            return 
        else:
            sleep(2)
            await client.send_message(chat, maling[tmp])
            return
            
    if 'Tidak ada harga' in event.text:
        sleep(2)
        await event.respond('/rumah_curiBarang')
        #print(tmp)
        return
      
    if 'Keamanan rumah yang' in event.text:
        sleep(2)
        tmp += 1
        
        if tmp == 10:
            await event.respond("4")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
        
    if 'tidak punya barang' in event.text:
        sleep(2)
        tmp += 1
        
        if tmp == 10:
            await event.respond("4")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
    
    if 'Rumah yang kamu kunjungi' in event.text:
        sleep(2)
        tmp += 1
        
        if tmp == 10:
            await event.respond("4")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return

    if 'Alamat yang sama' in event.text and curibarang:
        sleep(2)
        tmp += 1
        
        if tmp == 10:
            await event.respond("4")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        
        # return
        
    if 'Kamu terkurung' in event.text:
        sleep(2)
        await event.respond('/release')
        return
        
    if 'Bagus!!' in event.text:
        sleep(2)
        await event.respond('/rumah_curiBarang')
        return
        
    if 'kamu bebas sebebas' in event.text:
        sleep(2)
        await event.respond('/newaddressx_confirm')
        return
        
    if 'Apa kamu yakin' in event.text:
        sleep(2)
        await event.click(text="Confirm")
        return

    if 'Alamat diubah' in event.text:
        sleep(2)
        await event.respond('/rumah_curiBarang')
        return
    
    if 'Uuuh rasanya' in event.text:
        sleep(2)
        await event.respond(Masak)
        return
    
    if 'Berhasil memasak' in event.text:
        sleep(2)
        await event.respond(Masak)
        return
    
    if 'Kamu tidak bisa memasak' in event.text:
        curibarang = False
        curiduit = True
        # tmp = 0
        sleep(2)
        await event.respond('/rumah_curiBarang')
        return
        
    if 'Tidak cukup bahan' in event.text:
        sleep(2)
        await event.respond('/dapur_restock_MAX_confirm')
        return
    
    if 'Bahan-bahan direstock' in event.text:
        sleep(2)
        await event.respond(Masak)
        return
    
client.send_message(chat,'/rumah_curiBarang')

client.run_until_disconnected()
