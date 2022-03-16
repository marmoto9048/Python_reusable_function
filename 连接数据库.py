#!/usr/bin/python
# -*- coding: <utf-8> -*-
import pyodbc
import pandas as pd
import fcntl
def get_date_from_sql():
    connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.1633333;DATABASE=333 ;UID=sa;PWD=33333333')
    cursor = connect.cursor()
    # sql="SELECT A.製造NO AS ロットNo, A.品目KEY, A.品目CD, B.子品目KEY, B.子品目CD, A.指示数 AS 数量, B.実払出数 AS 所要数, B.手挿加工内容 AS 備考,  1 AS 前加工有無 FROM D_HR払出計画データ AS A INNER JOIN D_HR払出構成データ AS B ON A.製造NO = B.製造NO WHERE A.製造NO = 2101563476 "
    sql="SELECT TOP(1) A.払出完了日付, A.払出完了時間 FROM D_HR払出計画データ AS A INNER JOIN D_HR払出構成データ AS B ON A.製造NO = B.製造NO WHERE ((A.払出完了日付 = 20211110 AND A.払出完了時間 > 1800 ) or (A.払出完了日付 >= 20211111 )) AND A.払出完了日付 <> 20991231 AND A.品目CD LIKE '%$' AND A.指示数 <> 0 ORDER BY A.払出完了日付 DESC, A.払出完了時間 DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    DF_results = pd.DataFrame([tuple(t) for t in results])
    DF_results.to_csv(path_or_buf="sql_lasttime_cmd.csv", header=False,  index=False,sep=';')
    cursor.close()
