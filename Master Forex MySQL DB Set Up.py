
# PLEASE READ ALL COMMENTS FOR PROPER FUNCTION OF THE PROGRAM

import pymysql
import time


# change the username to your root username, change the password to yours and change the db to the database you choose
connection = pymysql.connect(host="localhost", user="root", password="Rodsader1*", db="forextrade")
cursor = connection.cursor()

currency_trade_name = input("Which currency trade do you want to create tables for \n (use [currency code 1]/[currency code 2] format; example: JPY/USD): (click then type next to here -->)   ")


sql_create_closing_table_command = "create table (%s)_closingprice (closingprice_id int primary key auto_increment, closepricedata decimal(5,4))"
sql_create_opening_table_command = "create table (%s)_openingprice (openingprice_id int primary key auto_increment, openpricedata decimal(5,4))"
sql_create_timestamp_table_command = "create table (%s)_timestampe (timestamp_id int primary key auto_increment, timestampdata varchar(30))"
sql_create_toptrendline_table_command = "create table (%s)_toptrendline (toptrendlinevalue_id int primary key auto_increment, toptrendlinedata decimal(5,4))"
sql_create_bottomtrendline_table_command = "create table (%s)_bottomtrendline (bottomtrendlinevalue_id int primary key auto_increment, bottomtrendlinedata decimal(5,4))"

# disbale these following two lines if you already have created the sample trend line graph tables
sql_create_sampleTrendLineGraph_table_command = "create table Sample_TrendLine_Graph (sample_static_data_id int primary key auto_increment, sample_data decimal(5,4))"
sql_create_sampleTopTrendLineGraph_table_command = "create table Sample_TopTrendLine_Graph (sample_top_data_id int primary key auto_increment, sample_top_data decimal(5,4))"
sql_create_sampleBottomTrendLineGraph_table_command = "create table Sample_BottomTrendLine_Graph (sample_bottom_data_id int primary key auto_increment, sample_bottom_data decimal(5,4))"

# disbale these following three lines if you already have created the database and activated its use
cursor.execute(sql_create_database_command)
cursor.execute(sql_use_database_command)
connection.commit()

# disbale these following four lines if you already have created the sample trend line graph tables
cursor.execute(sql_create_sampleTrendLineGraph_table_command)
cursor.execute(sql_create_toptrendline_table_command)
cursor.execute(sql_create_sampleBottomTrendLineGraph_table_command)
connection.commit()

cursor.execute(sql_create_closing_table_command, currency_trade_name)
cursor.execute(sql_create_opening_table_command, currency_trade_name)
cursor.execute(sql_create_timestamp_table_command, currency_trade_name)
cursor.execute(sql_create_toptrendline_table_command, currency_trade_name)
cursor.execute(sql_create_bottomtrendline_table_command, currency_trade_name)
connection.commit()

connection.close()

