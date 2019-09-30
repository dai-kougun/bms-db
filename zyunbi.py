import pandas as pd
import csv
from datetime import datetime

now = datetime.now()

cnt = 0
data = pd.read_csv("nanido.csv").values.tolist()

songs = []
for i in range(26):
    songs.append({})

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

    data = [title, level, grade]
    data_kakikomi = {hash_bms: data}
    print(data_kakikomi)
    df = pd.DataFrame(data_kakikomi)
    df.to_csv('zyunbi.scv')

now1 = datetime.now()
delta = now1 - now
delta1 = str(delta)
delta2 = delta1[:-7]
print("経過時間は"+delta2+"でした")
'''
        if(level<26):
            songs[level-1][hash_bms] = data
        else:
            songs[25][hash_bms] = data
'''