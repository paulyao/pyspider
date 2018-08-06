#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from six import itervalues
import mysql.connector

class SQL():
    #���ݿ��ʼ��
    def __init__(self):
        #���ݿ����������Ϣ
        hosts    = '127.0.0.1'  
        username = ''
        password = ''
        database = ''
        charsets = 'utf8'
        port=3318

        self.connection = False
        try:
            self.conn = mysql.connector.connect(host = hosts,user = username,passwd = password,db = database,port=port,charset = charsets)
            self.cursor = self.conn.cursor()
            self.cursor.execute("set names "+charsets)
            self.connection = True
        except Exception,e:
            print "Cannot Connect To Mysql!/n",e

    def escape(self,string):
        return '%s' % string
    #�������ݵ����ݿ�   
    def replace(self,tablename=None,**values):

        if self.connection: 
            tablename = self.escape(tablename)  
            if values:
                _keys = ",".join(self.escape(k) for k in values)
                _values = ",".join(['%s',]*len(values))
                sql_query = "replace into %s (%s) values (%s)" % (tablename,_keys,_values)
            else:
                sql_query = "replace into %s default values" % tablename
            try:
                if values:
                    self.cursor.execute(sql_query,list(itervalues(values)))
                else:       
                    self.cursor.execute(sql_query)
                self.conn.commit()
                return True
            except Exception,e:
                print "An Error Occured: ",e
                return False

    def select(self,tablename,colums,where):
        if self.connection: 
            tablename = self.escape(tablename)  
            if colums:
                sql_query ="select %s from %s %s;" % (colums,tablename,where)
            try:
                self.cursor.execute(sql_query)
                return self.cursor.fetchall()
            except Exception,e:
                print "An Error Occured: ",e
                return None
