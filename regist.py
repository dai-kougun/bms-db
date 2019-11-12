import csv
import cgi
import hash_song as hs
from datetime import datetime
import sqlite3 as sql
import json
now = datetime.now()
print(now)

database = 'mei_shisou.db'

#score = [[ "タイトル(差分名)", "発狂難易度", "判定ランク", "クリアタイプ", "スコアランク", "EXスコア", "perfect", "great", "good", "bad", "poor", "maxcombo", "最小BP", "プレイ回数", "スコアレート"]]
score = []
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sc = ['<img src="score/F.png">','<img src="score/F.png">', '<img src="score/E.png">', '<img src="score/D.png">', '<img src="score/C.png">', '<img src="score/B.png">', '<img src="score/A.png">', '<img src="score/AA.png">', '<img src="score/AAA.png">']
cl = ['<img src="clear/np.png">','<img src="clear/fd.png">', '<img src="clear/ec.png">', '<img src="clear/"cl.png>', '<img src="clear/hc.png">', '<img src="clear/fc.png">']
songs = [hs.hosi_0, hs.hosi_1, hs.hosi_2, hs.hosi_3, hs.hosi_4, hs.hosi_5, hs.hosi_6, hs.hosi_7, hs.hosi_8, hs.hosi_9, hs.hosi_10, hs.hosi_11, hs.hosi_12, hs.hosi_13, hs.hosi_14, hs.hosi_15, hs.hosi_16, hs.hosi_17, hs.hosi_18, hs.hosi_19, hs.hosi_20, hs.hosi_21, hs.hosi_22, hs.hosi_23, hs.hosi_24, hs.hosi_25]
ju = ['<img src="judge/ES.png">', '<img src="judge/NO.png">', '<img src="judge/HD.png">', '<img src="judge/VH.png">']
for i in range(26):
    for song in songs[i]:
        score.append([song[0], i, song[1], song[2], "None", "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

con = sql.connect(database)
cur = con.cursor()
cur.execute("select hash, clear, perfect, great, good, bad, poor, totalnotes, maxcombo, minbp, playcount, rank, rate from score;")
res = cur.fetchall()
data = list(res)



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
            judge = column[3]
            if(judge == "EASY"):
                column[3] = ju[0]
            elif(judge == "NORMAL"):
                column[3] = ju[1]
            elif(judge == "HARD"):
                column[3] = ju[2]
            else:
                column[3] = ju[3]
for row in score:
    row.pop(0)
    '''
with open('score_6.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(score)
    '''

html_string = '''
<!DOCTYPE html>
  <head>
  <meta charset="UTF-8">
  <title>発狂BMS score sheet</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/css/theme.default.min.css">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/jquery.tablesorter.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/extras/jquery.metadata.min.js"></script>
<!-- 追加機能(widgets)を使用する場合は次も追加する -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/jquery.tablesorter.widgets.min.js"></script>
<script type="text/javascript" src="tablesorter.js"></script>
</head>
<body>
  <p>This is your score.</p>
  <table id="myTable" class="tablesorter">
    <thead>
    <tr>
      <th>Ex</th>
      <th>title</th>
      <th>judge</th>
      <th>clear</th>
      <th>rank</th>
      <th>EX</th>
      <th>perfect</th>
      <th>great</th>
      <th>good</th>
      <th>bad</th>
      <th>poor</th>
      <th>combo</th>
      <th>minBP</th>
      <th>count</th>
      <th>rate</th>      
    </tr>
  </thead>
  <tbody>
'''
for li in score:
    row='<tr class="ex_' + str(li[0]) + '" align="right">\n'
    for e in li:
        row+="<td>%s</td>\n"%e
    row+="</tr>"
    html_string+=row
html_string+= '''
</tbody>
</table>
</body>
</html>
'''

with open('riamu.html', 'w') as f:
    f.write(html_string)

now1 = datetime.now()
delta = now1 - now
delta1 = str(delta)
delta2 = delta1[:-7]
print("経過時間は"+delta2+"でした")
