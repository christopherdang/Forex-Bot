from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib.pyplot as plt
import time
import pymysql
import smtplib

connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")

def sql_grabber_and_trendline_generator():

    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
    b = 1

    print("Enter a start point for the bottom trend line")
    userchoice = float(input('Type start point here for the bottom trend line-->   '))
    global newuser
    newuser = userchoice - 1.6000
    print(newuser)

    print("Enter a start point for the top trend line")
    userchoice2 = float(input('Type start point here for the top trend line-->   '))
    global newuser2
    newuser2 = userchoice2
    print(newuser2)

    while b == 1:

        for i in range(30):
            api_key = '1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f'
            cc = ForeignExchange(key=api_key)
            global data
            data, _ = cc.get_currency_exchange_intraday(from_symbol='EUR', to_symbol='USD', interval="1min", outputsize='compact')

            converteddata = str(data)
            global cursor
            connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
            cursor = connection.cursor()
            sql3 = "insert into testtoptrendline(testtoptrendlinedata) values (%s)"
            sql4 = "insert into testbottomtrendline(testbottomtrendlinedata) values (%s)"
            sql5 = "insert into testtimeprice(testimedata) values (substring(%s from 10794 for 19))"
            sql6 = "insert into testcloseprice(testclosedata) values (substring(%s from 10892 for 6))"
            sql7 = "insert into testopenprice(testopendata) values (substring(%s from 10829 for 6))"
            sql8 = "select testclosedata from testcloseprice order by id desc limit 1"
            sql12 = "select testtoptrendlinedata from testtoptrendline order by id desc limit 1"
            sql13 = "insert into testtriggerz(testanswer) values (%s)"
            sql10 = "select testopendata from testopenprice order by id desc limit 1"

            newuser = newuser + 0.0264
            newuser2 = newuser2
            cursor.execute(sql4, newuser)
            cursor.execute(sql3, newuser2)
            cursor.execute(sql5, converteddata)
            cursor.execute(sql6, converteddata)
            cursor.execute(sql7, converteddata)
            print("insert successful")
            connection.commit()
            cursor.execute(sql8)
            cursor.execute(sql10)
            cursor.execute(sql12)
            cursor.execute(sql13)
            cursor.execute()
            if cursor.execute(sql8) >= cursor.execute(sql3):
                print("closing price is above top trend line")
            elif cursor.execute(sql8) <= cursor.execute(sql3):AAAAAAAAAAAAAAAAAAAA
        print("1 cycle done")
        time.sleep(600)
        continue

email_username = 'saderod2@gmail.com'
email_password = 'suspectsaderod1*'

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
        print("Email Sent")


def breakDOWNalerttest():
    global connection
    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
    cursor = connection.cursor()
    sql8 = "select testclosedata from testcloseprice order by id desc limit 1"
    sql12 = "select testtoptrendlinedata from testtoptrendline order by id desc limit 1"
    sql13 = "insert into testtriggerz(testanswer) values (%s)"
    sql10 = "select testopendata from testopenprice order by id desc limit 1"
    yescomment = "yes"
    nocomment = "no"
    closevalues = []
    cursor.execute(sql8)
    for row in cursor.fetchall():
        closevalues.append(row[0])
    toplinevalues = []
    cursor.execute(sql12)
    for roww in cursor.fetchall():
        toplinevalues.append(roww[0])
    openvalues = []
    cursor.execute(sql10)
    for rowzz in cursor.fetchall():
        openvalues.append(rowzz[0])
    if float(closevalues[0]) <= float(toplinevalues[0]):
        cursor.execute(sql13, yescomment)
        connection.commit()
    elif float(openvalues[0]) <= float(toplinevalues[0]):
        cursor.execute(sql13, yescomment)
        connection.commit()
    else:
        cursor.execute(sql13, nocomment)
        connection.commit()

    triggerz = []
    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
    cursor = connection.cursor()
    sql14 = "select testanswer from testtriggerz order by id desc limit 1"
    cursor.execute(sql14)
    for rowww in cursor.fetchall():
        triggerz.append(rowww[0])
    if triggerz[0] == "yes":
        email_notif()
        print("went below trendline")
    else:
        print("still above trendline")

    time.sleep(60)

    while True:
        closevalues = []
        cursor.execute(sql8)
        for row in cursor.fetchall():
            closevalues.append(row[0])
        toplinevalues = []
        cursor.execute(sql12)
        for roww in cursor.fetchall():
            toplinevalues.append(roww[0])
        openvalues = []
        cursor.execute(sql10)
        for rowzz in cursor.fetchall():
            openvalues.append(rowzz[0])
        if float(closevalues[0]) <= float(toplinevalues[0]):
            cursor.execute(sql13, nocomment)
            connection.commit()
            print("still below trendline")
        elif float(openvalues[0]) <= float(toplinevalues[0]):
            cursor.execute(sql13, nocomment)
            connection.commit()
            print("still below trendline")
        else:
            email_notif()
            print("went above trendline")
            break

        time.sleep(60)

    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
    cursor = connection.cursor()
    sql8 = "select testclosedata from testcloseprice order by id desc limit 1"
    sql12 = "select testtoptrendlinedata from testtoptrendline order by id desc limit 1"
    sql13 = "insert into testtriggerz(testanswer) values (%s)"
    sql10 = "select testopendata from testopenprice order by id desc limit 1"
    yescomment = "yes"
    nocomment = "no"
    closevalues = []
    cursor.execute(sql8)
    for row in cursor.fetchall():
        closevalues.append(row[0])
    toplinevalues = []
    cursor.execute(sql12)
    for roww in cursor.fetchall():
        toplinevalues.append(roww[0])
    openvalues = []
    cursor.execute(sql10)
    for rowzz in cursor.fetchall():
        openvalues.append(rowzz[0])
    if float(closevalues[0]) >= float(toplinevalues[0]):
        cursor.execute(sql13, nocomment)
        connection.commit()
    elif float(openvalues[0]) >= float(toplinevalues[0]):
        cursor.execute(sql13, nocomment)
        connection.commit()
    else:
        cursor.execute(sql13, yescomment)
        connection.commit()

    triggerz = []
    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
    cursor = connection.cursor()
    sql14 = "select testanswer from testtriggerz order by id desc limit 1"
    cursor.execute(sql14)
    for rowww in cursor.fetchall():
        triggerz.append(rowww[0])
    if triggerz[0] == "yes":
        email_notif()
        print("went below trendline")
    else:
        print("still above trendline")

    time.sleep(60)

    while True:
        closevalues = []
        cursor.execute(sql8)
        for row in cursor.fetchall():
            closevalues.append(row[0])
        toplinevalues = []
        cursor.execute(sql12)
        for roww in cursor.fetchall():
            toplinevalues.append(roww[0])
        openvalues = []
        cursor.execute(sql10)
        for rowzz in cursor.fetchall():
            openvalues.append(rowzz[0])
        if float(closevalues[0]) >= float(toplinevalues[0]):
            cursor.execute(sql13, nocomment)
            connection.commit()
            print("still above trendline")
        elif float(openvalues[0]) >= float(toplinevalues[0]):
            cursor.execute(sql13, nocomment)
            connection.commit()
            print("still above trendline")
        else:
            email_notif()
            print("went below trendline, ignore the next email")
            break

        time.sleep(60)
        continue

a = 1

while a == 1:
    for i in range(30):
        sql_grabber_and_trendline_generator()
        time.sleep(60)
    print("1 cycle down")
    time.sleep(600)
    continue


connection.close()




