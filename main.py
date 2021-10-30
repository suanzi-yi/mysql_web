# -*- coding: utf-8 -*-
# @Time : 2021/10/29 20:40
# @Author : suanzi
# @Site : 
# @File : main.py
# @Software: PyCharm
#核心框架
from flask import Flask
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template
#插件
import flask_script
import flask_bootstrap
#web表单
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
#数据库操作模块
import sql_connect

#初始化对象
sqlweb=Flask(__name__)
bootstrap = flask_bootstrap.Bootstrap(sqlweb)#HTML模板
manager = flask_script.Manager(sqlweb)#命令行解析器
sqlweb.config['SECRET_KEY']='wocao'
#表单对象
class sqlform(Form):
    sql=StringField('请输入SQL语句',validators=[Required()])
    submit=SubmitField('确认')

#路由表
@sqlweb.route('/')
def index():
    session['database']=sql_connect.sqlcon('show databases')
    session['table']=sql_connect.sqlcon('show tables')
    return render_template('index.html',databse=session.get('database'),table=session.get('table'))

@sqlweb.route('/read',methods=['GET','POST'])
def read():
    form=sqlform()
    if form.validate_on_submit():
        sql_line=form.sql.data
        session['sql']=sql_connect.sqlcon(sql_line)
        return redirect(url_for('read'))
    return render_template('read.html',form=form,sql=session.get('sql'))

@sqlweb.route('/write',methods=['GET','POST'])
def write():
    form = sqlform()
    if form.validate_on_submit():
        sql_line = form.sql.data
        session['sql'] = sql_connect.sqlcon(sql_line)
        return redirect(url_for('write'))
    return render_template('write.html', form=form,status='OK')

#错误处理
@sqlweb.route('/<name>')
def err(name):
    if name:
        return redirect('/')

if __name__=='__main__':
    manager.run()