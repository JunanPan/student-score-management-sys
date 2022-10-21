# -*- coding: utf-8 -*-
import pymssql

# reload(sys)
import importlib, sys

importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
class SQLSearch1(object):
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = pymssql.connect(
                host='DESKTOP-T0AVUQU',
                user='sa',
                password='07280201Weng',
                database='studentdbs',
                charset="utf8"
                )
        except pymssql.Error as e:
            print("Error:%s" % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymssql.Error as e:
            print("Error:%s" % e)

    def select(self,x,table,address = ''):
        if address == '':
            sql = 'SELECT ' + str(x) + ' FROM ' + str(table)
        else:
            sql = 'SELECT ' + str(x) + ' FROM ' + str(table) + ' WHERE ' + str(address)
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        result = []
        while row:
            result.append(list(row))
            row = cur.fetchone()

        return result

    def insert(self,into,values):
        sql = 'INSERT INTO ' + str(into) + ' VALUES' + str(values)
        print(sql)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            print('INSERT ERROR')
            self.conn.rollback()


    def update(self,table,set,address):
        sql = 'UPDATE ' + str(table) + ' SET ' + str(set) + ' WHERE ' + str(address)
        print(sql)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            print('UPDATE ERROR')
            self.conn.rollback()


    def delete(self,table,address):
        sql = 'DELETE FROM ' + str(table) + ' WHERE ' + str(address)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            print('DELETE ERROR')
            self.conn.rollback()

    def sql(self,sql):
        print(sql)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            print('ERROR')
            self.conn.rollback()

