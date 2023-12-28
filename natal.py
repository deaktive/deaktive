import time
from telethon import TelegramClient, events, utils, Button

api_id = 1998603
api_hash = '341eb9d72c2de53ef2e70269728d5fca'

sesi_file = 'clon2'
bot_id = 'KampungMaifamXBot'
start = '/xm2022_GudangSanta'
ngumpul = 'KumpulkanHadiah'

normalHadiah = ['Balon', 'LayangLayang', 'Bola', 'PapanCatur', 'Kacamata', 'Topi']
rareHadiah = ['GaunPrincess', 'MobilMainan', 'Sepatu', 'Ransel', 'RobotMainan', 'BonekaBeruang']
uniqueHadiah = ['XS5', 'Ipong']

starting = True
buang = False

def buangHadiah(pesan):
    men = '/200)'
    mx = pesan.find(men) + len(men) + 2
    lmx = pesan.find('/xm2022_GudangSanta_buang', mx) - 2
    tex = pesan[mx:lmx]
    stex = tex.split()
    # print(stex)
    
    buang = []
    for i in range(len(stex)):
        ju = []
        for j in normalHadiah:
            if stex[i] == j:
                ju.append(stex[i])
                ju.append(stex[i+1])
                buang.append(ju)

        for j in rareHadiah:
            if stex[i] == j:
                ju.append(stex[i])
                ju.append(stex[i+1])
                buang.append(ju)
                
        for j in uniqueHadiah:
            if stex[i] == j:
                ju.append(stex[i])
                ju.append(stex[i+1])
                buang.append(ju)
    # print(buang)

    cmd = '/xm2022_buang_'
    cmdbuang = []
    for i in range(len(buang)):
        for j in normalHadiah:
            if buang[i][0] == j:
                inj = int(buang[i][1][0:(len(buang[i][1])-1)])
                if inj > 10:
                    ygbuang = inj-10
                    tes = cmd+buang[i][0]+'_'+str(ygbuang)+'_confirm'
                    cmdbuang.append(tes)

        for j in rareHadiah:
           if buang[i][0] == j:
                inj = int(buang[i][1][0:(len(buang[i][1])-1)])
                if inj > 20:
                    ygbuang = int(inj)-20
                    tes = cmd+buang[i][0]+'_'+str(ygbuang)+'_confirm'
                    cmdbuang.append(tes)
                    
        # for j in uniqueHadiah:
        #     if stex[i] == j:
        #         ju.append(stex[i])
        #         ju.append(stex[i+1])
        #         buang.append(ju)

    # print(cmdbuang)

    return cmdbuang
    
def jumlahKesempatan(pesan):
    se = 'mengumpulkan'
    sef = pesan.find(se) + len(se)
    lsef = pesan.find(',', sef)
    te = pesan[sef:lsef]
    ste = te.split()
    jumlahHadiah = int(ste[0])

    se2 = 'tersisa:'
    sef2 = pesan.find(se2) + len(se2) + 1
    lsef2 = pesan.find('=', sef2) - 2
    tex = pesan[sef2:lsef2]
    kesempatan = int(tex)
    # print(kesempatan)

    return jumlahHadiah, kesempatan



with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, start))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global jumlahHadiah, kesempatan, starting, cmdbuang, buang

        if starting:
            time.sleep(10)
            starting = False
            await event.click(text=ngumpul)
            return
            
        if 'Kamu mencari-cari di' in pesan:
            # menemukanHadiah(pesan)
            jumlahHadiah, kesempatan = jumlahKesempatan(pesan)
            print('hadiah = ', jumlahHadiah, '\t kesempatan = ', kesempatan)
            # buangHadiah(pesan)
            if jumlahHadiah < 190:
                time.sleep(10)
                await event.click(text=ngumpul)
            else:
                time.sleep(2)
                await event.respond(start)
            
            return
        
        if not buang and 'Daftar hadiah yang sudah didapat'  in pesan:
            buang = True
            cmdbuang = buangHadiah(pesan)
            print(cmdbuang)
            time.sleep(2)
            await event.respond('/xm2022_GudangSanta_buang')
            return

        if  '/xm2022_buang_' in pesan:
            for i in cmdbuang:
                time.sleep(3)
                print(i)
                await event.respond(i)
            
            time.sleep(2)
            starting = True
            buang = False
            await event.respond(start)
            return



client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')