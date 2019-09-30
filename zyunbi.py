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
    row0 = row[0].strip("{ }")
    row1 = row[1].strip("{ }")
    row2 = row[2]
    level = row2
    info = row0 + ":" +row1
    if(level<26):
        songs[level-1].append(info)
    else:
        songs[25].append(info)
for i in range(26):
    print(songs[i])

with open('zyunbi.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(songs)
now1 = datetime.now()
delta = now1 - now
delta1 = str(delta)
delta2 = delta1[:-7]
print("経過時間は"+delta2+"でした")