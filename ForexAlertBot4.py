from alpha_vantage.foreignexchange import ForeignExchange
import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from pprint import pprint
import time
import pymysql
import numpy as np
import matplotlib.dates as mdates

plt.style.use("fivethirtyeight")

def grap_api_data():
    api_key = '1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f'
    cc = ForeignExchange(key=api_key)
    global data
    data, _ = cc.get_currency_exchange_intraday(from_symbol='EUR', to_symbol='USD', interval="1min", outputsize='compact')

def sql_insert_sequence():
    converteddata = str(data)
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
    cursor = connection.cursor()
    sql5 = "insert into timeprice(timedata) values (substring(%s from 10794 for 19))"
    sql6 = "insert into closeprice(closedata) values (substring(%s from 10892 for 6))"
    sql7 = "insert into openprice(opendata) values (substring(%s from 10829 for 6))"
    cursor.execute(sql5, converteddata)
    cursor.execute(sql6, converteddata)
    cursor.execute(sql7, converteddata)
    print("insert successful" + sql5)
    connection.commit()

listloop = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

for i in listloop:
    grap_api_data()
    sql_insert_sequence()
    time.sleep(60)

time.sleep(600)

for m in listloop:
    grap_api_data()
    sql_insert_sequence()
    time.sleep(60)

connection.close()



