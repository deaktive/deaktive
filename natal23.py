import time
from telethon import TelegramClient, events, utils, Button
from datetime import datetime

api_id = 1998603
api_hash = '341eb9d72c2de53ef2e70269728d5fca'

sesi_file = 'dexter'
bot_id = 'KampungMaifamXBot'
cek = "/xm2023_barang"
ngumpul = 'KumpulkanHadiah'
# item, maks, init
hadiah = [
    ["iPong15ProMag", 20, 0],
    ["XS", 20, 0],
    ["GaunPrincess", 40, 0],
    ["BonekaBeruang", 40, 0],
    ["Ransel", 20, 0],
    ["Topi", 15, 0],
    ["Sepatu", 20, 0],
    ["Bola", 20, 0],
    ["KaosKaki", 15, 0],
    ["RobotMainan", 40, 0],
    ["MobilMainan", 40, 0],
    ["LayangLayang", 15, 0],
    ["PapanCatur", 15, 0],
    ["Balon", 15, 0],
    ["Piyama", 15, 0]
]

gudang = ["/xm2023_GudangSanta_1", "/xm2023_GudangSanta_2", "/xm2023_GudangSanta_3", "/xm2023_GudangSanta_4", "/xm2023_GudangSanta_5"]
home = "/xm2023_GudangSanta"

pilihgudang = input("nomer gudang (1/2/3/4/5) : ")
pilihangudang = int(pilihgudang) - 1

cmd = ["Cari", "Curi", "Cari Hadiah", "Ambil"]

def cekhadiah(pesan, hadiah):
    ff = "kumpulkan:"
    f = pesan.find(ff) + len(ff)
    ll = "Kamu bisa"
    l = pesan.find(ll, f) - 1

    teks = pesan[f:l].split()
    # print(teks)

    for i in range(len(teks)):
        for j in range(len(hadiah)):
            if hadiah[j][0] == teks[i]:
                p = teks[i+1]
                # print(p)
                jumlah = int(p[0:(len(p)-1)])
                hadiah[j][2] = jumlah

    return hadiah

def pilihhadiah(pesan, hadiah):
    ff = "sebuah"
    f = pesan.find(ff) + len(ff)
    l = pesan.find(",", f)
    teks = pesan[f:l].split()
    print("\n", teks)

    cmdpil = ""

    for i in range(len(teks)):
        for j in range(len(hadiah)):
            if hadiah[j][0] in teks[i]:
                if hadiah[j][2] < hadiah[j][1]:
                    cmdpil = cmd[3]
                else :
                    cmdpil = cmd[2]
                break
    
    return cmdpil

def cekdapet(pesan, hadiah):
    ff = "mengambil"
    f = pesan.find(ff) + len(ff)
    ll = "Cek"
    l = pesan.find(ll, f) - 1
    teks = pesan[f:l].split()

    for i in range(len(teks)):
        for j in range(len(hadiah)):
            if hadiah[j][0] in teks[i]:
                hadiah[j][2] += 1

    return hadiah

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, cek))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        timestamp = datetime.now().strftime("%H:%M:%S")
        global hadiah

        if "Daftar hadiah yang sudah kamu kumpulkan" in pesan:
            hadiah = cekhadiah(pesan, hadiah)
            print(hadiah)
            time.sleep(2.5)
            await event.respond(home)
            return
        
        if "Hadiah akan direset tiap" in pesan:
            time.sleep(8.5)
            await event.click(text=cmd[2])
            return
        
        if "dan dari jauh melihat" in pesan:
            # skip nyolong
            time.sleep(8.5)
            await event.click(text=cmd[2])
            return
        
        if "dan menemukan sebuah" in pesan:
            # nemu barang
            cmdnya = pilihhadiah(pesan, hadiah)
            print(cmdnya)
            time.sleep(3.5)
            await event.click(text=cmdnya)
            return

        if "Berhasil mengambil" in pesan:
            hadiah = cekhadiah(pesan, hadiah)
            print("\n", timestamp, "\n", hadiah)
            time.sleep(8.5)
            await event.click(text=cmd[2])
            return
        
        if "Pelan-pelan," in pesan:
            print("\n\tKecepetan!!")
            time.sleep(8.5)
            await event.click(text=cmd[2])
            return
        
        if "Terlambat!!" in pesan:
            print("\n\tKecepetan!!")
            time.sleep(8.5)
            await event.click(text=cmd[2])
            return




client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')