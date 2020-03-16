def sql_grabber_and_trendline_generator():

    global connection
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

    belowTrendline = False
    aboveTrendline = False

    while b == 1:

        for i in range(30):
            api_key = '1456af4c4704e5e6bd4b60c30094b56b-32c375f91dc677c9fce0916d50811d4f'
            cc = ForeignExchange(key=api_key)
            global data
            data, _ = cc.get_currency_exchange_intraday(from_symbol='EUR', to_symbol='USD', interval="1min", outputsize='compact')

            converteddata = str(data)
            global connection
            global cursor
            connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
            cursor = connection.cursor()
            sql3 = "insert into testtoptrendline(testtoptrendlinedata) values (%s)"
            sql4 = "insert into testbottomtrendline(testbottomtrendlinedata) values (%s)"
            sql5 = "insert into testtimeprice(testimedata) values (substring(%s from 10794 for 19))"
            sql6 = "insert into testcloseprice(testclosedata) values (substring(%s from 10892 for 6))"
            sql7 = "insert into testopenprice(testopendata) values (substring(%s from 10829 for 6))"

            print("insert successful")
            newuser = newuser + 0.0264
            newuser2 = newuser2
            cursor.execute(sql4, newuser)
            cursor.execute(sql3, newuser2)
            cursor.execute(sql5, converteddata)
            cursor.execute(sql6, converteddata)
            cursor.execute(sql7, converteddata)
            connection.commit()

            belowTrendline = emailNotifBottomTrendline(sql6, sql7, sql4, belowTrendline)

            aboveTrendline = emailNotifTopTrendline(sql6, sql7, sql3, aboveTrendline)

            time.sleep(60)
        print("1 cycle done")
        time.sleep(600)
        continue

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