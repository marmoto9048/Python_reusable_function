#!/usr/bin/python
# -*- coding: <utf-8> -*-
import pyodbc
import pandas as pd
def get_date_from_sql():
    connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.163.333.3;DATABASE=333 ;UID=xx;PWD=33333333')
    cursor = connect.cursor()
    sql="SELECT xxxx from xxxx"
    cursor.execute(sql)
    results = cursor.fetchall()
    DF_results = pd.DataFrame([tuple(t) for t in results])
    DF_results.to_csv(path_or_buf="sql_lastime_cmd.csv", header=False,  index=False,sep=';')
    cursor.close()
