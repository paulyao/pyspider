#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEText import MIMEText 

class Mail:
    def __init__(self):
        self.to_list=['totoro_china@163.com','ymei@grasp.com.cn','yifei.wang@163.com','waiwofei@qq.com','yfei@grasp.com.cn','bcdej@vip.qq.com','756503247@qq.com','316428218@qq.com','471055325@qq.com','whli@grasp.com.cn']
        
        
    def send_mail(self,name,content):  
        self.Subject=name+u'公告更新提醒'
        self.me=u'公告小爬虫 <SecRobot@grasp.com.cn>'
        self.msg = MIMEText(content,_subtype='html',_charset='UTF-8') 
        self.msg['Subject'] = self.Subject
        self.msg['From'] = self.me  
        self.msg['To'] = ','.join(self.to_list)
        try:  
            server = smtplib.SMTP()  
            server.connect("smtp.grasp.com.cn")  
            server.login("SecRobot@grasp.com.cn","5134543545+ffagasdfgdfg")  
            server.sendmail(self.me, self.to_list, self.msg.as_string())  
            server.close()  
            return True  
        except Exception, e:  
            print str(e)  
        return False