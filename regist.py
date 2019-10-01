import csv
import cgi
import hash_song as hs
from datetime import datetime
import sqlite3 as sql
now = datetime.now()
print(now)

database = 'O4RO.db'

score = [[ "タイトル(差分名)", "発狂難易度", "判定ランク", "クリアタイプ", "スコアランク", "EXスコア", "perfect", "great", "good", "bad", "poor", "maxcombo", "最小BP", "プレイ回数", "スコアレート"]]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sc = ["None","F", "E", "D", "C", "B", "A", "AA", "AAA"]
cl = ["Null","Failed", "Easy", "Clear", "Hard", "FC"]
songs = [hs.hosi_0, hs.hosi_1, hs.hosi_2, hs.hosi_3, hs.hosi_4, hs.hosi_5, hs.hosi_6, hs.hosi_7, hs.hosi_8, hs.hosi_9, hs.hosi_10, hs.hosi_11, hs.hosi_12, hs.hosi_13, hs.hosi_14, hs.hosi_15, hs.hosi_16, hs.hosi_17, hs.hosi_18, hs.hosi_19, hs.hosi_20, hs.hosi_21, hs.hosi_22, hs.hosi_23, hs.hosi_24, hs.hosi_25]

for i in range(26):
    for song in songs[i]:
        score.append([song[0], song[1], i, song[2], "None", "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

con = sql.connect(database)
cur = con.cursor()
cur.execute("select hash, clear, perfect, great, good, bad, poor, totalnotes, maxcombo, minbp, playcount, rank, rate from score;")
res = cur.fetchall()
data = list(res)

print(data)

for row in data:
    hash_id = row[0]
    for column in score:
        if hash_id in column:
            column[4] = cl[row[1]]
            column[5] = sc[row[11]]
            ex = row[2] * 2 + row[3]
            column[6] = ex
            column[7] = row[2]
            column[8] = row[3]
            column[9] = row[4]
            column[10] = row[5]
            column[11] = row[6]
            combo = str(row[8]) + "/" + str(row[7])
            column[12] = combo
            column[13] = row[9]
            column[14] = row[10]
            rat = (ex*100) / (row[7]*2)
            rate = round(rat, 2)
            column[15] = rate
cnt = 0
for row in score:
    if(cnt == 0):
        cnt += 1
        continue
    row.pop(0)
with open('score_5.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(score)

now1 = datetime.now()
delta = now1 - now
delta1 = str(delta)
delta2 = delta1[:-7]
print("経過時間は"+delta2+"でした")