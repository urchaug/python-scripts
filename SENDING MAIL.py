# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:59:34 2018

@author: Urchaug
"""

#!/usr/bin/python
import smtplib
sender = 'abc@senddomain.com'
receivers = ['xyz@recdomain.com']
message = """"from: from person <abc@senddomain.com>
To: To person <xyz@recdomain.com>
subject: SMTP e-mail message.
""""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message)
    print ("mail sent successfully")
except SMTPException:
    print("error in sending mail")
    
    