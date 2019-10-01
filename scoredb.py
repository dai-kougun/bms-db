# 必要モジュールをインポートする
import sqlite3
import csv
import pandas as pd


with sqlite3.connect("23k_tekubi.db") as connection:
    csvWriter = csv.writer(open("output.csv", "w"))
    c = connection.cursor()
    rows = c.fetchall()
    for row in rows:
    # do your stuff
        csvWriter.writerow(row)