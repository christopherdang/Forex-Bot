import time
import pymysql


# listloop = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
listloop = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def choose_start_point():
    print("Enter a start point")
    userchoice = float(input('Type start point here-->   '))
    global newuser
    newuser = userchoice
    print(newuser)
    for i in listloop:
        newuser = newuser
        print(newuser)
        connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
        cursor = connection.cursor()
        sql5 = "insert into trendlinetop(toptrendlinedata) values (%s)"
        cursor.execute(sql5, newuser)
        connection.commit()
        print("insert successful")



# def sql_insert_sequence():
#     global connection
#     connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
#     cursor = connection.cursor()
#     sql5 = "insert into trendline(trendlinedata) values (%s)"
#     cursor.execute(sql5, newuser)
#     print("insert successful")
#     connection.commit()

choose_start_point()
# sql_insert_sequence()

