import time
import asyncio
import sys
import threading
import telethon
import re
from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 19426024
api_hash = '93e64ab1fca196717682f11b879b9214'
sesi_fil = 'dextervps'

besiList = [
'/makan_rotibelanda',
'/furnace_1_add_confirm',
'/furnace_2_add_confirm',
'/furnace_3_add_confirm',
'/furnace_4_add_confirm',
'/furnace_5_add_confirm',
'/furnace_6_add_confirm',
'/furnace_7_add_confirm',
'/furnace_8_add_confirm',
'/furnace_9_add_confirm',
'/furnace_10_add_confirm',
'/furnace_11_add_confirm',
'/furnace_12_add_confirm',
'/furnace_13_add_confirm',
'/furnace_14_add_confirm',
'/furnace_15_add_confirm',
'/furnace_16_add_confirm',
'/furnace_17_add_confirm',
'/furnace_18_add_confirm',
'/furnace_19_add_confirm',
'/furnace_20_add_confirm',
'/furnace_21_add_confirm',
'/furnace_22_add_confirm',
'/furnace_23_add_confirm',
'/furnace_24_add_confirm',
'/furnace_25_add_confirm',
'/furnace_26_add_confirm',
'/furnace_27_add_confirm',
'/furnace_28_add_confirm',
'/furnace_29_add_confirm',
'/furnace_30_add_confirm',
'/furnace_31_add_confirm',
'/furnace_32_add_confirm',
'/furnace_33_add_confirm',
'/furnace_34_add_confirm',
'/furnace_35_add_confirm',
'/furnace_36_add_confirm',
'/furnace_37_add_confirm',
'/furnace_38_add_confirm',
'/furnace_39_add_confirm',
'/furnace_40_add_confirm',
'/furnace_41_add_confirm',
'/furnace_42_add_confirm',
'/furnace_43_add_confirm',
'/furnace_44_add_confirm',
'/furnace_45_add_confirm',
'/furnace_46_add_confirm',
'/furnace_47_add_confirm',
'/furnace_48_add_confirm',
'/furnace_49_add_confirm',
'/furnace_50_add_confirm',
'/furnace_51_add_confirm',
'/furnace_52_add_confirm',
'/furnace_53_add_confirm',
'/furnace_54_add_confirm',
'/furnace_55_add_confirm',
'/furnace_56_add_confirm',
'/furnace_57_add_confirm',
'/furnace_58_add_confirm',
'/furnace_59_add_confirm',
'/furnace_60_add_confirm',
'/furnace_61_add_confirm',
'/furnace_62_add_confirm',
'/furnace_63_add_confirm',
'/furnace_64_add_confirm',
'/furnace_65_add_confirm',
'/furnace_66_add_confirm',
'/furnace_67_add_confirm',
'/furnace_68_add_confirm',
'/furnace_69_add_confirm',
'/furnace_70_add_confirm',
'/furnace_71_add_confirm',
'/furnace_72_add_confirm',
'/furnace_73_add_confirm',
'/furnace_74_add_confirm',
'/furnace_75_add_confirm',
'/furnace_76_add_confirm',
'/furnace_77_add_confirm',
'/furnace_78_add_confirm',
'/furnace_79_add_confirm',
'/furnace_80_add_confirm',
'/furnace_81_add_confirm',
'/furnace_82_add_confirm',
'/furnace_83_add_confirm',
'/furnace_84_add_confirm',
'/furnace_85_add_confirm',
'/furnace_86_add_confirm',
'/furnace_87_add_confirm',
'/furnace_88_add_confirm',
'/furnace_89_add_confirm',
'/furnace_90_add_confirm',
'/furnace_91_add_confirm',
'/furnace_92_add_confirm',
'/furnace_93_add_confirm',
'/furnace_94_add_confirm',
'/furnace_95_add_confirm',
'/furnace_96_add_confirm',
'/furnace_97_add_confirm',
'/furnace_98_add_confirm',
'/furnace_99_add_confirm',
'/furnace_100_add_confirm',
'/furnace_101_add_confirm',
'/furnace_102_add_confirm',
'/furnace_103_add_confirm',
'/furnace_104_add_confirm',
'/furnace_105_add_confirm',
'/furnace_106_add_confirm',
'/furnace_107_add_confirm',
'/furnace_108_add_confirm',
'/furnace_109_add_confirm',
'/furnace_110_add_confirm',
'/furnace_111_add_confirm',
'/furnace_112_add_confirm',
'/furnace_113_add_confirm',
'/furnace_114_add_confirm',
'/furnace_115_add_confirm',
'/furnace_116_add_confirm',
'/furnace_117_add_confirm',
'/furnace_118_add_confirm',
'/furnace_119_add_confirm',
'/furnace_120_add_confirm',
'/furnace_121_add_confirm',
'/furnace_122_add_confirm',
'/furnace_123_add_confirm',
'/furnace_124_add_confirm',
'/furnace_125_add_confirm',
'/furnace_126_add_confirm',
'/furnace_127_add_confirm',
'/furnace_128_add_confirm',
'/furnace_129_add_confirm',
'/furnace_130_add_confirm',
'/furnace_131_add_confirm',
'/furnace_132_add_confirm',
'/furnace_133_add_confirm',
'/furnace_134_add_confirm',
'/furnace_135_add_confirm',
'/furnace_136_add_confirm',
'/furnace_137_add_confirm',
'/furnace_138_add_confirm',
'/furnace_139_add_confirm',
'/furnace_140_add_confirm',
#'/furnace_141_add_confirm',
#'/furnace_142_add_confirm',
#'/furnace_143_add_confirm',
#'/furnace_144_add_confirm',
#'/furnace_145_add_confirm',
#'/furnace_146_add_confirm',
#'/furnace_147_add_confirm',
#'/furnace_148_add_confirm',
#'/furnace_149_add_confirm',
#'/furnace_150_add_confirm',
'/seedMaker_1_anggurkeramatsss_confirm',
'/seedMaker_2_anggurkeramatsss_confirm',
'/seedMaker_3_anggurkeramatsss_confirm',
'/seedMaker_4_anggurkeramatsss_confirm',
'/seedMaker_5_anggurkeramatsss_confirm',
'/seedMaker_6_anggurkeramatsss_confirm',
'/seedMaker_7_anggurkeramatsss_confirm',
'/seedMaker_8_anggurkeramatsss_confirm',
'/seedMaker_9_anggurkeramatsss_confirm',
'/seedMaker_10_anggurkeramatsss_confirm',
'/seedMaker_11_anggurkeramatsss_confirm',
'/seedMaker_12_anggurkeramatsss_confirm',
'/seedMaker_13_anggurkeramatsss_confirm',
'/seedMaker_14_anggurkeramatsss_confirm',
'/seedMaker_15_anggurkeramatsss_confirm',
'/seedMaker_16_anggurkeramatsss_confirm',
'/seedMaker_17_anggurkeramatsss_confirm',
'/seedMaker_18_anggurkeramatsss_confirm',
'/seedMaker_19_anggurkeramatsss_confirm',
'/seedMaker_20_anggurkeramatsss_confirm',
'/seedMaker_21_anggurkeramatsss_confirm',
'/seedMaker_22_anggurkeramatsss_confirm',
'/seedMaker_23_anggurkeramatsss_confirm',
'/seedMaker_24_anggurkeramatsss_confirm',
'/seedMaker_25_anggurkeramatsss_confirm',
'/seedMaker_26_anggurkeramatsss_confirm',
'/seedMaker_27_anggurkeramatsss_confirm',
'/seedMaker_28_anggurkeramatsss_confirm',
'/seedMaker_29_anggurkeramatsss_confirm',
'/seedMaker_30_anggurkeramatsss_confirm',
'/seedMaker_31_anggurkeramatsss_confirm',
'/seedMaker_32_anggurkeramatsss_confirm',
'/seedMaker_33_anggurkeramatsss_confirm',
'/seedMaker_34_anggurkeramatsss_confirm',
'/seedMaker_35_anggurkeramatsss_confirm',
#'/seedMaker_36_anggurkeramatsss_confirm',
#'/seedMaker_37_anggurkeramatsss_confirm',
#'/seedMaker_38_anggurkeramatsss_confirm',
#'/seedMaker_39_anggurkeramatsss_confirm',
#'/seedMaker_40_anggurkeramatsss_confirm',

'Last',
]

Grade = [
'',
'Last',
]

mese = '/mf_furnace'
thebot = "KampungMaifamxBot"
mer = 0
gradenum = 0

def Dexter():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(sesi_fil, api_id, api_hash, loop=loop) as clien:
        clien.loop.run_until_complete(clien.send_message('KampungMaifamxBot', mese))

        @clien.on(events.NewMessage(from_users='KampungMaifamxBot'))
        async def handler(event):
            global mer
            global idMer
            global gradenum
            
            if "yang kamu pesan" in event.raw_text:
                mer += 0
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "BatanganBesi" in event.raw_text:
                mer += 0
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "Furnace level" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "Pengolahan selesai!!" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "bibit selesai" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "progress pembuatan bibit" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "mampu menghasilkan" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "Berhasil memasukkan" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if 'Kamu tidak memiliki' in event.raw_text:
                time.sleep(2)
                await event.respond('/restore_max_confirm')
                return

            if "Uuuh rasanya enak" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

            if "Tidak tidak" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return

#            if 'Sudah jadi!!' in event.raw_text:
#                time.sleep(2)
#                await event.respond('/mf_Furnace_3')
#                return

#            if 'Berhasil menaruh' in event.raw_text:
#                time.sleep(2)
#                await event.respond('/addTitle_MachinaryExpert')
#                return

#            if 'gelar pada' in event.raw_text:
#                time.sleep(2)
#                await event.respond('/mf_Furnace')
#                return

#            if 'tungku kecil' in event.raw_text:
#                time.sleep(2)
#                await event.click(text=Beli)
#                return

            if besiList[mer] == besiList[-1]:
                gradenum +=0
                mer = 0
                print('Selesai Semua')
                time.sleep(2)
                await event.respond(''+besiList[mer]+Grade[gradenum])
                return
            
            if Grade[gradenum] == Grade[-1]:
                gradenum = 0
                mer = 0
                print('Diulang')
                time.sleep(2)
                await event.respond(mese)
                return

        clien.run_until_disconnected()
        print(time.asctime(), '-', 'Stop')

threading.Thread(target=Dexter).start()
print(time.asctime(), '-', 'Start')

#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
