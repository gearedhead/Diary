from flask import Flask, render_template
from flask import request
from datetime import datetime
import sqlite3
import json
conn=sqlite3.connect('master.db',check_same_thread=False)

#Defining Functions for SQL Queries
def sql_query(query):
    cur=conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()
    return rows
namelist=[]
namelisttmb=[]
names=sql_query('select NAME from Customer_Account_Details')
namestmb=sql_query('select NAME from Customer_Account_Details_TMB')
for i in range(len(names)):
    namelist.append(names[i][0])
    i+=1
for i in range(len(namestmb)):
    namelisttmb.append(namestmb[i][0])
    i+=1






app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html',namelist=namelist,namelisttmb=namelisttmb)

@app.route('/result',methods=['POST','GET'])
def print_data():
 if request.method=='POST':
     result=request.form['data']
     res=sql_query('select * from Customer_Account_Details where NAME ='+"'"+result+"'")
     return render_template('result.html',res=res)

@app.route('/resulttmb',methods=['POST','GET'])
def print_datatmb():
 if request.method=='POST':
     resulttmb=request.form['datatmb']
     restmb=sql_query('select * from Customer_Account_Details_TMB where NAME ='+"'"+resulttmb+"'")
     return render_template('resulttmb.html',restmb=restmb)
 



if __name__ =="__main__":
    app.run(host='192.168.42.187', port=8000)
