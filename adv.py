import time, asyncio, sys, random, threading
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_file = "arlenop"

bot_id = 'GrandPiratesBot'
exp_pil = 0

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def delay0():
    now = time.localtime()
    menit = now.tm_min
    detik = now.tm_sec
    if menit == 0 and detik == 0:
        return
    delay_sec = (60 - menit) * 60 - detik
    time.sleep(delay_sec)

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, "Adventure"))

    @client.on(events.NewMessage(from_users = bot_id))
    async def handler(event):
        global exp_pil
        pesan = event.raw_text
        
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
        
        if "KAMU MENANG!!" in pesan:
            exp_pil += 1
            if exp_pil > 10:
                time.sleep(2)
                await event.respond("/use_EXPPill_10")
                return
            else:
                print(time.asctime())
                time.sleep(1)
                await event.click(0,0)
                return
            return
        
        if "Musuh menang" in pesan:
            time.sleep(2)
            await event.respond('/restore')
            return
        
        if "Energi krumu" in pesan:
            time.sleep(2)
            await event.respond('/restore')
            return
        
        if "kondisi yang prima" in pesan:
            time.sleep(1)
            await event.click(0,0)
            return
        
        if "Berhasil memulihkan" in pesan:
            time.sleep(2)
            await event.respond("/levelupKapal_ATK")
            return
        
        if "Kapalmu masih memerlukan" in pesan:
            time.sleep(1)
            await event.respond("Adventure")
            return
        
        if "Apa kamu yakin ingin meningkatkan" in pesan:
            time.sleep(1)
            await event.click(0,0)
            await event.respond("Adventure")
            return
        
        if "Kamu mendapat hadiah" in pesan:
            time.sleep(2)
            await event.respond('Adventure')
            return
            
        if "Kamu sudah mencapai batas" in pesan:
            delay0()
            await event.respond("Adventure")
            return
        
        if "Berhasil menggunakan 💊EXPPill" in pesan:
            exp_pil = 0 
            
            time.sleep(2)
            await event.respond("Adventure")
            return
        
        if 'Pertandingan belum usai' in pesan:
            time.sleep(2)
            await event.click(0,0)
            return
        
        elif "EastBlue: ShellsTown" in pesan or "EastBlue: OrangeTown" in pesan or "EastBlue: SyrupVillage" in pesan or "EastBlue: Baratie" in pesan or "EastBlue: ArlongPark" in pesan or "EastBlue: Loguetown" in pesan or "EastBlue: TwinCapes" in pesan or "GrandLine: WhiskyPeak" in pesan or "GrandLine: LittleGarden" in pesan or "GrandLine: WinterSea" in pesan or "GrandLine: DrumIsland" in pesan or "Alabasta: Nanohana" in pesan or "Alabasta: Erumalu" in pesan or "Alabasta: SandoraDesert" in pesan or "Alabasta: SpiderCafe" in pesan or "Alabasta: Rainbase" in pesan or "Alabasta: Alubarna" in pesan or "Paradise: RulukaIsland" in pesan or "Paradise: GoatIsland" in pesan or "Paradise: FireworksIsland" in pesan or "Paradise: PineappleIsland" in pesan or "Jaya: JayaSea" in pesan or "Jaya: MockTown" in pesan:

            time.sleep(1)
            await event.click(0,0)
            return
        
    client.start()
    print("Dimulai!")
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stop')