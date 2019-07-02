#!/usr/bin/python3
# from django.http import HttpResponse
# from django.shortcuts import render
import pymysql
# db = pymysql.connect('192.168.2.10','cmdb','cmdb','cmdb')
# cur = db.cursor()
# sql = "INSERT into DEVICE (NAME,IP,TYPE,PORT,USER,PASSWORD,DESCRIPTION,PRODUCTION) values ('server3','192.168.2.20',1,22,'root','admin','','')"
# cur.execute(sql)
# db.commit()
class deviceManage:
    def __init__(self,DBHOST,DBUSER,DBPASSWORD,DBNAME):
        self.DBHOST = DBHOST
        self.DBUSER = DBUSER
        self.DBPASSWORD = DBPASSWORD
        self.DBNAME = DBNAME
        return

    #deviceInfo is (NAME,IP,TYPE,PORT,USER,PASSWORD,DESCRIPTION,PRODUCTION)
    #time：2019/6/30 author:wf
    #function：add device
    def addDevice(self,deviceInfo):
        db = pymysql.connect(self.DBHOST,self.DBUSER,self.DBPASSWORD,self.DBNAME)
        cursor = db.cursor()
        sql1 = "ALTER TABLE DEVICE AUTO_INCREMENT = 1"
        cursor.execute(sql1)
        sql = "INSERT into DEVICE (NAME,IP,TYPE,PORT,USER,PASSWORD,DESCRIPTION,PRODUCTION) values "+ deviceInfo
        cursor.execute(sql)
        db.commit()
        db.close()
        return

    #time：2019/6/30 author:wf
    #使用ID删除设备
    def delDevice(self,ID):
        db = pymysql.connect(self.DBHOST, self.DBUSER, self.DBPASSWORD, self.DBNAME)
        cursor = db.cursor()
        sql = "delete from DEVICE where ID=" + str(ID)
        cursor.execute(sql)
        sql1 = "ALTER TABLE DEVICE AUTO_INCREMENT=" + str(ID)
        cursor.execute(sql1)
        db.commit()
        db.close()
        return

    #time：2019/6/30 author:wf
    #搜索设备信息：只能通过IP，NAME搜索,NAME支持模糊搜索，IP只支持精确搜索
    def searchDevice(self, item, search):
        db = pymysql.connect(self.DBHOST, self.DBUSER, self.DBPASSWORD, self.DBNAME)
        cursor = db.cursor()
        if item == 'IP':
            sql = 'select * from DEVICE where IP="' +search + '"'
            cursor.execute(sql)
            data = cursor.fetchall()
        elif item == 'NAME':
            sql = 'select * from DEVICE where NAME like "%' + search +'%"'
            cursor.execute(sql)
            data = cursor.fetchall()
        else:
            data = ""
        db.close()
        return data













p = deviceManage('192.168.2.10','cmdb','cmdb','cmdb')
li = ('server5','192.168.2.20',1,22,'root','admin','','')
# p.addDevice(str(li))
# data = p.searchDevice('IP','192.168.2.20')
p.delDevice(3)
# print(data)



# def hello1(request):
#     # mesage = request.GET('ip')
#     return render(request,'index.html')
#
# def hello2(request):
#     return HttpResponse("hello2")
