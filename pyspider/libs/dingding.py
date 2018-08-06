#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json,urllib2
import datetime

class DingTalk:
    def send_msg(self,content):
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        textmod={"msgtype": "text","text": {"content":nowTime+' | '+ content},"at": {"atMobiles": [],"isAtAll":"false"}}
        textmod = json.dumps(textmod)
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
        url='https://oapi.dingtalk.com/robot/send?access_token=39b87e5df2111731e65f80842036deb6848dfdc9ed07e7c2ee8b9fb55f23c234'
        req = urllib2.Request(url=url,data=textmod,headers=header_dict)
        res = urllib2.urlopen(req)
        res = res.read()
        print(res)