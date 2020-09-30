import sqlite3
import re
import collections.abc
conn=sqlite3.connect('master.db',check_same_thread=False)

#Defining Functions for SQL Queries
def sql_query(query):
    cur=conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()
    return rows
anish=sql_query("""Select * from Customer_Account_Details where NAME ='RAJENDRAN T'""");
for row in anish:
    print (row[4])

