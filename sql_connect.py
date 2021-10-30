# -*- coding: utf-8 -*-
# @Time : 2021/10/30 12:02
# @Author : suanzi
# @Site : 
# @File : sql_connect.py
# @Software: PyCharm

import pymysql
import json
def sqlcon(cell):
    conn=pymysql.connect(host='localhost',user='root',password='root',db='pikachu')
    cur=conn.cursor()
    sql='"'+str(cell)+'"'
    try:
        cur.execute(eval(sql))
        data=cur.fetchall()
        conn.commit()
    except:
        conn.rollback()
    return data
