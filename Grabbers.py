def api_infoJPY():
    api_key = "1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f"
    api_name = ForeignExchange(key=api_key)
    global JPYdata
    JPYdata, _ = api_name.get_currency_exchange_intraday(from_symbol="JPY", to_symbol="USD", interval="1min", outputsize="compact")
    global JPYjson
    JPYjson = str(JPYdata)

def sender_SQLJPY():
    JPYjson = str(JPYdata)
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="db_password", db="foreignExchange")
    cursor = connection.cursor()
    sql_time = "insert into timeTable(timeData) values *substring(%s from 10794 for 19))"
    sql_close = "insert into jpycloseprice(jpyclosePrice) values (substring(%s from 10892 for 6))"
    sql_open = "insert into jpyopenprice(jpyopenPrice) values *substring(%s from 10829 for 6))"
    cursor.execute(sql_time, JPYjson)
    cursor.execute(sql_close, JPYjson)
    cursor.execute(sql_open, JPYjson)
    print("insert successful")
    connection.commit()

def api_infoGBP():
    api_key = "1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f"
    api_name = ForeignExchange(key=api_key)
    global GBPdata
    GBPdata, _ = api_name.get_currency_exchange_intraday(from_symbol="GBP", to_symbol="USD", interval="1min", outputsize="compact")
    global GBPjson
    GBPjson = str(GBPdata)

def sender_SQLGBP():
    GBPjson = str(GBPdata)
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="db_password", db="foreignExchange")
    cursor = connection.cursor()
    sql_time = "insert into timeTable(timeData) values *substring(%s from 10794 for 19))"
    sql_close = "insert into gbpcloseprice(gbpclosePrice) values (substring(%s from 10892 for 6))"
    sql_open = "insert into gbpopenprice(gbpopenPrice) values *substring(%s from 10829 for 6))"
    cursor.execute(sql_time, GBPjson)
    cursor.execute(sql_close, GBPjson)
    cursor.execute(sql_open, GBPjson)
    print("insert successful")
    connection.commit()

def api_infCAD():
    api_key = "1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f"
    api_name = ForeignExchange(key=api_key)
    global CADdata
    CADdata, _ = api_name.get_currency_exchange_intraday(from_symbol="CAD", to_symbol="USD", interval="1min", outputsize="compact")
    global CADjson
    CADjson = str(CADdata)

def sender_SQLCAD():
    CADjson = str(CADdata)
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="db_password", db="foreignExchange")
    cursor = connection.cursor()
    sql_time = "insert into timeTable(timeData) values *substring(%s from 10794 for 19))"
    sql_close = "insert into cadcloseprice(cadclosePrice) values (substring(%s from 10892 for 6))"
    sql_open = "insert into cadopenprice(cadopenPrice) values *substring(%s from 10829 for 6))"
    cursor.execute(sql_time, CADjson)
    cursor.execute(sql_close, CADjson)
    cursor.execute(sql_open, CADjson)
    print("insert successful")
    connection.commit()

def api_infoCHF():
    api_key = "1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f"
    api_name = ForeignExchange(key=api_key)
    global CHFdata
    CHFdata, _ = api_name.get_currency_exchange_intraday(from_symbol="CHF", to_symbol="USD", interval="1min", outputsize="compact")
    global CHFjson
    CHFjson = str(CHFdata)

def sender_SQLCHF():
    CHFjson = str(CHFdata)
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="db_password", db="foreignExchange")
    cursor = connection.cursor()
    sql_time = "insert into timeTable(timeData) values *substring(%s from 10794 for 19))"
    sql_close = "insert into chfcloseprice(chfclosePrice) values (substring(%s from 10892 for 6))"
    sql_open = "insert into chfopenprice(chfopenPrice) values *substring(%s from 10829 for 6))"
    cursor.execute(sql_time, CHFjson)
    cursor.execute(sql_close, CHFjson)
    cursor.execute(sql_open, CHFjson)
    print("insert successful")
    connection.commit()