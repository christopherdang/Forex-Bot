import time
import pymysql
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="tyler_trade2")
cursor = connection.cursor()


def Sample_Trendline_Generator():
    topclearcommand = "truncate sample_toptrendline_graph"
    bottomclearcommand = "truncate sample_bottomtrendline_graph"
    connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="tyler_trade2")
    cursor = connection.cursor()
    cursor.execute(topclearcommand)
    connection.commit()
    cursor.execute(bottomclearcommand)
    connection.commit()
    startpointtop = float(input("Top trend line start point:   "))
    startpointbottom = float(input("Bottom trend line start point:   "))
    toptrendlinehighamount = float(input("How high up do you want the top trend line:   "))
    bottomtrendlinedropamount = float(input("How low do you want the bottom trend line:   "))
    toptrendlineincramount = float(input("How much should the top slope increase or decrease:   "))
    bottomtrendlineincramount = float(input("How much should the bottom slope increase or decrease:   "))
    sqlredraw_top = "insert into sample_toptrendline_graph(sample_top_data) values(%s)"
    sqlredraw_bottom = "insert into sample_bottomtrendline_graph(sample_bottom_data) values(%s)"

    new_top_start_point = startpointtop + toptrendlinehighamount
    new_bottom_start_point = startpointbottom - bottomtrendlinedropamount

    cursor.execute(sqlredraw_top, new_top_start_point)
    connection.commit()

    for i in range(5):
        new_top_start_point = new_top_start_point + toptrendlineincramount
        cursor.execute(sqlredraw_top, new_top_start_point)
        connection.commit()

    cursor.execute(sqlredraw_bottom, new_bottom_start_point)
    connection.commit()

    for i in range(5):
        new_bottom_start_point = new_bottom_start_point + bottomtrendlineincramount
        cursor.execute(sqlredraw_bottom, new_bottom_start_point)
        connection.commit()

    print("done")

Sample_Trendline_Generator()

connection.close()


