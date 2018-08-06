#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from pyspider.libs.mail import *

class File:
    def updatefile(self,name,notice):
        mail=Mail()
        self.file='E:\\notice\\'+name+'_notice.txt'
        if (os.path.exists(self.file)):
            f=open(self.file,'rt')
            s=f.read()
            f.close()
				
            if (s==notice):
                print 'notice not update!'
            else:
                f=open(self.file,'wt')
                f.write(notice)
                f.close()
                mail.send_mail(name,notice)
                print 'send mail done!'
        else:
			    f=open(self.file,'wt')
			    f.write(notice)
			    f.close()
			    mail.send_mail(name,notice)
			    print 'send mail done!'