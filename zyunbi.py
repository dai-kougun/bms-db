import pandas as pd
import csv
from datetime import datetime

now = datetime.now()

cnt = 0
data = pd.read_csv("nanido.csv").values.tolist()

songs = []
for i in range(26):
    songs.append([])

for row in data:
    hash_bms = row[0]
    title = row[1]
    if(title == 'Vantablack {color: #000000'):
        row2 = row[3]
        grade = row[4]
    else:
        row2 = row[2]
        grade = row[3]
    level = int(row2)
    data = [hash_bms,title,grade]
    if(level != 99):
        songs[level].append(data)
    else:
        songs[0].append(data)

with open("hash_song.txt", "w") as f:
    for i in range(26):
        song = map(str, songs[i])
        son = ','.join(song)
        f.write("hosi_" + str(i) + "=[")
        f.write(son)
        f.write("]\n")
        


now1 = datetime.now()
delta = now1 - now
delta1 = str(delta)
delta2 = delta1[:-7]
print("経過時間は"+delta2+"でした")
