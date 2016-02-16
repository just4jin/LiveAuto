#!/usr/bin/env 

import win32com.client
import smtplib
from time import localtime, strftime

def send_email(fm_load, fy_load, tm_load, ty_load, table_name):
    from_date= str(fm_load) + "/" + str(fy_load) 
    to_date= str(tm_load) + "/" + str(ty_load) 
    
    recipient = "***@***.com; ***@***.com"
    subject = "***"
    time_now = strftime("%Y-%m-%d %H:%M:%S", localtime())
    
    if (fm_load == tm_load) and (fy_load == ty_load):
	body = "Report %s in local database was out of sync for month %s. \
\n\nAs of %s, local database is up-to-date with ASPM website through %s. \n\nName" % (table_name, from_date, time_now, from_date)
    else:
	body = "Report %s in local database was out of sync with ASPM website for months from %s to %s. \
\n\nAs of %s, local database is up-to-date with ASPM website through %s. \n\nName" % (table_name, from_date, to_date, time_now, to_date)
    
    o = win32com.client.Dispatch("Outlook.Application")
    try:
        Msg = o.CreateItem(0)
        Msg.To = recipient
        Msg.Subject = subject
        Msg.Body = body
        Msg.Send()
        print '\nSuccessfully Sent Email Notice!'
    except:
        print "\nFailed to Send Email Notice!"
