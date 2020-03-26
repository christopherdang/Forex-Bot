
# PLEASE READ ALL COMMENTS FOR PROPER FUNCTION OF THE PROGRAM

import pymysql
import time


# change the username to your root username, change the password to yours and change the db to the database you choose
connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="tyler_trade2")
cursor = connection.cursor()

sql_create_closing_table_command = "create table USD_JPY_closingprice (id int primary key auto_increment, closepricedata decimal(5,4))"
sql_create_opening_table_command = "create table USD_JPYopeningprice (openingprice_id int primary key auto_increment, openpricedata decimal(5,4))"
sql_create_timestamp_table_command = "create table USD_JPY_timestamp (timestamp_id int primary key auto_increment, timestampdata varchar(30))"
sql_create_toptrendline_table_command = "create table USD_JPY_toptrendline (toptrendlinevalue_id int primary key auto_increment, toptrendlinedata decimal(5,4))"
sql_create_bottomtrendline_table_command = "create table USD_JPY_bottomtrendline (bottomtrendlinevalue_id int primary key auto_increment, bottomtrendlinedata decimal(5,4))"

# disable these following two lines if you already have created the sample trend line graph tables
sql_create_sampleTrendLineGraph_table_command = "create table Sample_TrendLine_Graph (sample_static_data_id int primary key auto_increment, sample_data decimal(5,4))"
sql_create_sampleTopTrendLineGraph_table_command = "create table Sample_TopTrendLine_Graph (sample_top_data_id int primary key auto_increment, sample_top_data decimal(5,4))"
sql_create_sampleBottomTrendLineGraph_table_command = "create table Sample_BottomTrendLine_Graph (sample_bottom_data_id int primary key auto_increment, sample_bottom_data decimal(5,4))"
sql_create_sampleTimeStampGraph_table_command = "create table sample_timestamp_graph (sample_timestamp_id int primary key auto_increment, sample_timestamp_data int)"
sql_insert_sample_command = "insert into Sample_TrendLine_Graph(sample_data) values (%s)"
sql_insert_sampletime_command = "insert into sample_timestamp_graph(sample_timestamp_data) values (%s)"
sample_value_1 = 1.0805
sample_value_2 = 1.0809
sample_value_3 = 1.0709
sample_value_4 = 1.0704
sample_value_5 = 1.0905
sample_value_6 = 1.0805
sample_time_1 = 1
sample_time_2 = 2
sample_time_3 = 3
sample_time_4 = 4
sample_time_5 = 5
sample_time_6 = 6


# disable these following four lines if you already have created the sample trend line graph tables
cursor.execute(sql_create_sampleTrendLineGraph_table_command)
connection.commit()
cursor.execute(sql_create_sampleTopTrendLineGraph_table_command)
connection.commit()
cursor.execute(sql_create_sampleBottomTrendLineGraph_table_command)
connection.commit()
cursor.execute(sql_insert_sample_command, sample_value_1)
connection.commit()
cursor.execute(sql_insert_sample_command, sample_value_2)
connection.commit()
cursor.execute(sql_insert_sample_command, sample_value_3)
connection.commit()
cursor.execute(sql_insert_sample_command, sample_value_4)
connection.commit()
cursor.execute(sql_insert_sample_command, sample_value_5)
connection.commit()
cursor.execute(sql_insert_sample_command, sample_value_6)
connection.commit()
cursor.execute(sql_insert_sampletime_command, sample_time_1)
cursor.execute(sql_insert_sampletime_command, sample_time_2)
cursor.execute(sql_insert_sampletime_command, sample_time_3)
cursor.execute(sql_insert_sampletime_command, sample_time_4)
cursor.execute(sql_insert_sampletime_command, sample_time_5)
cursor.execute(sql_insert_sampletime_command, sample_time_6)
connection.commit()


cursor.execute(sql_create_closing_table_command)
connection.commit()
cursor.execute(sql_create_opening_table_command)
connection.commit()
cursor.execute(sql_create_timestamp_table_command)
connection.commit()
cursor.execute(sql_create_toptrendline_table_command)
connection.commit()
cursor.execute(sql_create_bottomtrendline_table_command)
connection.commit()

connection.close()

