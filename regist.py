import pandas as pd
import requests
from bs4 import BeautifulSoup as bp 
import csv
import hash_song as hs
from datetime import datetime
now = datetime.now()

score = [["タイトル(差分名)", "発狂難易度", "判定ランク", "クリアタイプ", "スコアランク", "EXスコア", "perfect", "great", "good", "bad", "poor", "maxcombo", "最小BP", "プレイ回数", "スコアレート"]]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sc = ["None","F", "E", "D", "C", "B", "A", "AA", "AAA"]
cl = ["Null","Failed", "Easy", "Clear", "Hard", "FC"]
songs = [hs.hosi_1, hs.hosi_2, hs.hosi_3, hs.hosi_4, hs.hosi_5, hs.hosi_6, hs.hosi_7, hs.hosi_8, hs.hosi_9, hs.hosi_10, hs.hosi_11, hs.hosi_12, hs.hosi_13, hs.hosi_14, hs.hosi_15, hs.hosi_16, hs.hosi_17, hs.hosi_18, hs.hosi_19, hs.hosi_20, hs.hosi_21, hs.hosi_22, hs.hosi_23, hs.hosi_24, hs.hosi_25, hs.hosi_99]

for i in range(26):
    for song in songs[i]:
        score.append(songs[i][song])

cnt = 0
data = pd.read_csv("score.csv").values.tolist()
for row in data:
    hash_id = row[0]

    else:
        h1 = h1.get_text()
        combo = str(row[8]) + "/" + str(row[7])
        #count = str(row[11]) + "/" + str(row[12])
        td = list(soup.find_all("td"))
        hantei = td[3].string
        aa = list(soup.find_all("a"))
        insane = aa[9].string
        if not(isinstance(insane, type(None))):
            if(("★" in insane[:1]) and not("★" in insane[1:2])):
                insane = insane[1:]
                ex = row[2] * 2 + row[3]
                rate = (ex*100) / (row[7]*2) 
                rate = round(rate, 2)
                if("?" in insane):
                    insane = "★？"
                elif(insane[:1] in num):
                    insane = int(insane)
                    if(insane < 26):
                        insane = "★" + str(insane)
                    else:
                        print("This is not insane bms(over 26)")
                        continue
                parameter = [h1, insane, hantei, cl[row[1]], sc[row[13]], ex, row[2], row[3], row[4], row[5], row[6], combo, row[9], row[10], rate]
                score.append(parameter)

            else:
                print("This is not insane bms(not ★)")  
        else:
            print("This is not insane bms(type: None)")
    cnt += 1
    print("No."+str(cnt)+" is over.")
with open('score_2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(score)
now1 = datetime.now()
delta = now1 - now
delta1 = str(delta)
delta2 = delta1[:-7]
print("経過時間は"+delta2+"でした")
'''
html_string = 
<html>
  <head><meta charset="UTF-8">
  <title>bms score</title>
  </head>
  <link rel="stylesheet" type="text/css" href="mystyle.css"/>
  <body>
    {table}
  </body>
</html>.
'''


