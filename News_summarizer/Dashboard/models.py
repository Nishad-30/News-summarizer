from django.db import models

# Create your models here.

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="sahil@2004",database = "News")

mycursor = mydb.cursor()

# def tuple_to_list(tuple):
#     list_from_tuple = []
#     for i in tuple:
#         list_from_tuple.append(i)
#     return list_from_tuple

def nested_tuple_to_nested_list(tuple):
    list_from_tuple = []
    for i in tuple:
        inner_list = []
        for j in i:
            inner_list.append(j)
        list_from_tuple.append(inner_list)
    return list_from_tuple


def display_table(table_name):
    sql = "SELECT * FROM "+table_name
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    myresult = nested_tuple_to_nested_list(myresult)
    return myresult

def insert_into_table(table_name,data):
    sql = "INSERT INTO "+table_name+" VALUES ("+data+")"
    mycursor.execute(sql)
    mydb.commit()

def inserting(table_name,data,val):
    sql = "INSERT INTO "+table_name+" VALUES ("+data+")"
    mycursor.execute(sql, val)
    mydb.commit()

def selection_search(table_name,columen_name,value):
    sql = "SELECT * FROM "+table_name+" WHERE "+ columen_name+" = '"+value+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    myresult = nested_tuple_to_nested_list(myresult)
    return myresult

def update_values(table_name,column_name_1,value_1,column_name_2,value_2):
    sql = "UPDATE "+table_name+" SET "+column_name_1+" = '"+value_1+"' WHERE "+column_name_2+" = '"+value_2+"' and "+column_name_2+" = '"+value_2+"'"
    mycursor.execute(sql)
    mydb.commit()

def selection_searchs(table_name,column_name1,value1,column_name2,value2):
    sql = "SELECT * FROM "+table_name+" WHERE "+ column_name1+" = '"+value1+"' and "+ column_name2+" = '"+value2+"'"
    print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    myresult = nested_tuple_to_nested_list(myresult)
    return myresult


