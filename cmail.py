# import random
# import math
import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,body,subject):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('jagadeeshgudimetla04@gmail.com','xyii mfpu moca ydeb')
    msg=EmailMessage()
    msg['from']='jagadeeshgudimetla04@gmail.com'
    msg['to']=to
    msg['subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()

