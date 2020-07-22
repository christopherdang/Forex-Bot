# import pandas as pd
from alpha_vantage.foreignexchange import ForeignExchange
# import time
import pymysql
import smtplib

import os
db_password = os.environ.get('DB_PASSWORD')
email_username = os.environ.get('EMAIL_USERNAME')
email_password = os.environ.get('EMAIL_PASSWORD')

def email_notif():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_username, email_password)

        subject = 'Foreign exchange market update'
        body = 'Ready to sell/ buy!'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email_username, email_username, msg)

def api_info():
    api_key = "1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f"
    api_name = ForeignExchange(key=api_key)
    global data
    data, _ = api_name.get_currency_exchange_intraday(from_symbol="EUR", to_symbol="USD", interval="1min", outputsize="compact")
    global json
    json = str(data)

def sender_SQL():
    json = str(data)
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="db_password", db="foreignExchange")
    cursor = connection.cursor()
    sql_time = "insert into timeTable(timeData) values *substring(%s from 10794 for 19))"
    sql_close = "insert into closeprice(closePrice) values (substring(%s from 10892 for 6))"
    sql_open = "insert into openprice(openPrice) values *substring(%s from 10829 for 6))"
    cursor.execute(sql_time, json)
    cursor.execute(sql_close, json)
    cursor.execute(sql_open, json)
    print("insert successful")
    connection.commit()

# x = time values
# y = close values
# z = open values
# w = bottom line values
# v = top line values

#api_info()
#sender_SQL()

#connection.close()

email_notif()