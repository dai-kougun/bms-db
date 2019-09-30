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
        score.append([songs[i][song], i+1, "Null", "Null", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(score)