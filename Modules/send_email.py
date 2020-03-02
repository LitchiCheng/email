"""Simple operation for sending email.

Instead of importing lots of relative modules.
The "SMTPServe" class is a dictionary of smtp address of some Chinese Server.
The "SendEmail" class is used for logining, sending and so on.
""" 

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SMTPServe:
    dict = {"163":"smtp.163.com", "qq":"smtp.qq.com"}

class SendEmail:
    def __init__(self, usr_name, usr_pwd, usr_server):
        self.usr_name = usr_name
        self.usr_pwd = usr_pwd
        self.usr_server = usr_server
        self.msg = MIMEMultipart()          
        try:
            self.smtpObj = smtplib.SMTP_SSL(usr_server, 465)
            self.smtpObj.login(usr_name, usr_pwd) 
            self.__login = True
        except smtplib.SMTPException as e:
            self.__login = False
            print("login fail:" + str(e))

    def loginStatus(self):
        return self.__login

    def setSender(self, sdr_address):
        self.msg["From"] = "{}".format(sdr_address)

    def setReciever(self, rcr_address):
        self.msg["To"] = ",".join(rcr_address)
        self.reciever_list = rcr_address

    def setSubject(self, title):
        self.msg["Subject"] = title

    def addPlainContent(self, p_ct):
        self.msg.attach(MIMEText(p_ct, "plain", "utf-8"))
    
    def addHtmlContent(self, html):
        self.msg.attach(MIMEText(html, "html", "utf-8"))

    def addAttachFile(self, file_address):
        try:
            file_stream = open(file_address, "rb").read()
        except:
            print("load file fail.")
        ath = MIMEApplication(file_stream)
        file_name = file_address.split("\\")
        ath.add_header('Content-Disposition', 'attachment', filename=file_name[-1])
        self.msg.attach(ath)

    def sendEmail(self):
        try:
            self.smtpObj.sendmail(self.usr_name, self.reciever_list, self.msg.as_string()) 
            print("send successfully.")
            return True
        except smtplib.SMTPException as e:
            print("send fail:" + str(e))
            return False
 