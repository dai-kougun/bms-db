import pandas as pd
import aiohttp
from bs4 import BeautifulSoup as bp 
import csv
import asyncio
import async_timeout
import numpy as np
from datetime import datetime


score = [["タイトル(差分名)", "発狂難易度", "判定ランク", "クリアタイプ", "スコアランク", "EXスコア", "perfect", "great", "good", "bad", "poor", "maxcombo", "最小BP", "プレイ回数", "スコアレート"]]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
rank = ["None", "Easy", "Normal", "Hard", "FC"]
scrank = ["Null", "F", "E", "D", "C", "B", "A", "AA", "AAA"]

master_data = pd.read_csv("score.csv").values.tolist()

i = 0

async def get_html(session, url):
    with async_timeout.timeout(200):
        async with session.get(url) as response:
            return await response.text()


async def main(data):
    i = 0
    j = 0
    async with aiohttp.ClientSession() as session:
        while data:
            row = data.pop(0)
            hash_id = row[0]
            if len(hash_id) != 32:
                continue

            link = "http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsmd5=" + hash_id
            try:
                soup = bp(await get_html(session, link), "html.parser")
            except Exception:
                j += 1
                if(j > 10):
                    print("Can't get" + row[0])
                    break
                print("Error Count:" + str(j))
                data.append(row)
                continue
            i += 1
            print("No."+str(i)+' Done!')
            h1 = soup.find("h1")
            if isinstance(h1, type(None)):
                continue
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
                        parameter = [h1, insane, hantei, rank, scrank, ex, row[2], row[3], row[4], row[5], row[6], combo,
                                     row[9], row[10], rate]
                        score.append(parameter)
                    else:
                        print("This is not insane bms(not ★)")
                else:
                    print("This is not insane bms(type: None)")
    



def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx+n]


if __name__ == '__main__':
    now = datetime.now()
    print("now:"+str(now))
    loop = asyncio.get_event_loop()

    coroutines = [main(data) for data in split_list(master_data, 10)]
    futures = asyncio.gather(*coroutines)
    loop.run_until_complete(futures)
    with open('score_2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(score)
    loop.close()
    now1 = datetime.now()
    now2 = now1 - now
    now2 = str(now2)
    now2 = now2[:-7]
    print("かかった時間:"+ now2) 

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


