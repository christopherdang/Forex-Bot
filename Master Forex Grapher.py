import time
import pymysql
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
cursor = connection.cursor()

sql8 = "select graphdata from graphbutton"
sql9 = "select graphtopdata from graphtop"
sql10 = "select graphbottomdata from graphbottom"
sql11 = "select graphtimedata from graphtime"

def animate(i):
    global graphvalues
    graphvalues = []
    cursor.execute(sql8)
    for row in cursor.fetchall():
        graphvalues.append(row[0])

    global toptrendline
    toptrendline = []
    cursor.execute(sql9)
    for rowz in cursor.fetchall():
        toptrendline.append(rowz[0])

    global bottomtrendline
    bottomtrendline = []
    cursor.execute(sql10)
    for rowzz in cursor.fetchall():
        bottomtrendline.append(rowzz[0])

    global xaxis
    xaxis = []
    cursor.execute(sql11)
    for rowzz in cursor.fetchall():
        xaxis.append(rowzz[0])

    global x
    global y
    global z
    global w
    global v

    x = xaxis
    y = graphvalues
    z = toptrendline
    w = bottomtrendline

    plt.plot(x, y, label="Price Data")
    plt.plot(x, z, label="Top Trend  Line")
    plt.plot(x, w, label=" Bottom Trend Line")
    plt.legend(loc="upper left")

Sample_Trendline_Generator()
ani = FuncAnimation(plt.gcf(), animate, interval=60000)
plt.show()

connection.close()


