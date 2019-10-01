import pandas as pd
import requests
from bs4 import BeautifulSoup as bp 
import csv
from datetime import datetime
now = datetime.now()
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sc = ["None","F", "E", "D", "C", "B", "A", "AA", "AAA"]
cl = ["Null","Failed", "Easy", "Clear", "Hard", "FC"]


i = 0
score = []
cnt = 0
data = pd.read_csv("score.csv").values.tolist()
for row in data:
    #hash_id = row.pop(row[0])
    hash_id = row[0]
    if len(hash_id) != 32:
        continue
    link = "http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsmd5=" + hash_id
    r = requests.get(link)
    soup = bp(r.content, "html.parser")
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
                    insane = 99
                elif(insane[:1] in num):
                    insane = int(insane)
                    if(insane < 26):
                        i += 1
                        print(i)
                    else:
                        print("This is not insane bms(over 26)")
                        continue
                parameter = [row[0], h1, insane, hantei]
                score.append(parameter)

            else:
                print("This is not insane bms(not ★)")  
        else:
            print("This is not insane bms(type: None)")
    cnt += 1
    print("No."+str(cnt)+" is over.")
with open('nanido.csv', 'w') as f:
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


