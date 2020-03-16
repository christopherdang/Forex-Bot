import time
import pymysql
import smtplib


connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
cursor = connection.cursor()

belowTrendline = False
aboveTrendline = False



def emailNotifBottomTrendline(dataPointClosing, dataPointOpening, bottomTrendlinePoint, belowLine):
    _dataPointClosing = dataPointClosing
    _dataPointOpening = dataPointOpening
    _dataPointFinal = 0

    if _dataPointClosing < _dataPointOpening:
        _dataPointFinal = _dataPointClosing
    else:
        _dataPointFinal = _dataPointOpening

    _bottomTrendlinePoint = bottomTrendlinePoint
    _belowLine = belowLine

    if not _belowLine:
        if _dataPointFinal <= _bottomTrendlinePoint:
            _belowLine = True
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(email_username, email_password)

                subject = 'Foreign exchange market update'
                body = 'Ready to sell/ buy!'
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(email_username, email_password, msg)
                print("Email Sent")
        else:
            _belowLine = False

    else:
        if _dataPointFinal >= _bottomTrendlinePoint:
            _belowLine = False
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(email_username, email_password)

                subject = 'Foreign exchange market update'
                body = 'Ready to sell/ buy!'
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(email_username, email_password, msg)
                print("Email Sent")
        else:
            _belowLine = True

    return _belowLine



def emailNotifTopTrendline(dataPointClosing, dataPointOpening, topTrendlinePoint, aboveLine):
    _dataPointClosing = dataPointClosing
    _dataPointOpening = dataPointOpening
    _dataPointFinal = 0

    if _dataPointClosing < _dataPointOpening:
        _dataPointFinal = _dataPointClosing
    else:
        _dataPointFinal = _dataPointOpening

    _topTrendlinePoint = topTrendlinePoint
    _aboveLine = aboveLine

    if not _aboveLine:
        if _dataPointFinal >= _topTrendlinePoint:
            _aboveLine = True
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(email_username, email_password)

                subject = 'Foreign exchange market update'
                body = 'Ready to sell/ buy!'
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(email_username, email_password, msg)
                print("Email Sent")
        else:
            _aboveLine = False

    else:
        if _dataPointFinal <= _topTrendlinePoint:
            _aboveLine = False
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(email_username, email_password)

                subject = 'Foreign exchange market update'
                body = 'Ready to sell/ buy!'
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(email_username, email_word, msg)
                print("Email Sent")
        else:
            _aboveLine = True

    return _aboveLine

closeprice = 5
openingprice1 = 4
openingprice2 = 9
openingprice3 = 11
bottomtrendline = 2
toptrendline = 10

sqlttt = "insert into testtoptrendline3(testtoptrendlinedata) values (%s)"
sqlbtt = "insert into testbottomtrendline3(testbottomtrendlinedata) values (%s)"
sqlcp = "insert into testcloseprice3(testclosedata) values (%s)"
sqlop = "insert into testopenprice3(testopendata) values (%s)"

belowTrendline = emailNotifBottomTrendline(sqlcp, sqlop, sqlbtt, belowTrendline)

aboveTrendline = emailNotifTopTrendline(sqlcp, sqlop, sqlttt, aboveTrendline)


cursor.execute(sqlbtt, bottomtrendline)
connection.commit()

cursor.execute(sqlttt, toptrendline)
connection.commit()

cursor.execute(sqlcp, closeprice)
connection.commit()

cursor.execute(sqlop, openingprice1)
connection.commit()

belowTrendline = emailNotifBottomTrendline(sqlcp, sqlop, sqlbtt, belowTrendline)

aboveTrendline = emailNotifTopTrendline(sqlcp, sqlop, sqlttt, aboveTrendline)

##################################

cursor.execute(sqlbtt, bottomtrendline)
connection.commit()

cursor.execute(sqlttt, toptrendline)
connection.commit()

cursor.execute(sqlcp, closeprice)
connection.commit()

cursor.execute(sqlop, openingprice2)
connection.commit()

belowTrendline = emailNotifBottomTrendline(sqlcp, sqlop, sqlbtt, belowTrendline)

aboveTrendline = emailNotifTopTrendline(sqlcp, sqlop, sqlttt, aboveTrendline)

##################################

cursor.execute(sqlbtt, bottomtrendline)
connection.commit()

cursor.execute(sqlttt, toptrendline)
connection.commit()

cursor.execute(sqlcp, closeprice)
connection.commit()

cursor.execute(sqlop, openingprice3)
connection.commit()

belowTrendline = emailNotifBottomTrendline(sqlcp, sqlop, sqlbtt, belowTrendline)

aboveTrendline = emailNotifTopTrendline(sqlcp, sqlop, sqlttt, aboveTrendline)

connection.close()