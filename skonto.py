import time
import requests
import time
from ShazamAPI import Shazam
import json
from datetime import datetime
import sys, os


stream_url = 'http://stream.radioskonto.lv/mp3'

r = requests.get(stream_url, stream=True)

z = 0
text_old = ""
text=""


while  z == 0:
    t_end = time.time() + 10
#ievac 10sek garu skanas gabalu
    with open('stream.mp3', 'wb') as f:
        try:
            for block in r.iter_content(1024):
                f.write(block)
                if time.time() > t_end:
                    break
        except KeyboardInterrupt:
            pass
    print("skana dabuta")
    try:
        mp3_file = open('stream.mp3', 'rb').read()
        shazam = Shazam(mp3_file)
        dziesma = shazam.recognizeSong()
        tek = str((next(dziesma)))

    except:
        print("#################### NEIET NETS #############")
                #########")
        time.sleep(60)
        next

    if len(tek) < 200:
        print("REKLAMA")
    else:
        print("DZIESMA ATRASTA")

    try:
#Sitais murgs lai dabutu dziesmu ara ka stringu, sorry
        tek = tek[tek.find('title'):]
        tek = tek.split('images')[0]
        tek = tek[:-3]
        tek = tek.replace("title", "").replace("sub", "").replace(":", "").replace("'", "").replace('"', '')
        song, artist = tek.split(",")
        text = (artist + " - " + song)
    except:
        next

#pieliek klat datumu un saglaba teksta faila
    if text != text_old:
        laiks = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        today = datetime.today().strftime('%d-%m-%Y')
        filepath = 'skonto_list.txt'
        item =  str(laiks)+ " * "+ text
        with open(filepath, 'a') as f:
            f.write("%s\n" % item)
        print(item)
    else:
        print("Skan tas pats!")
    text_old = text
    print("********** GULU 60 sekundes ************")
    time.sleep(60)









