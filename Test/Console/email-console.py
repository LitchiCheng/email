
import os,configparser,sys

modules_path = (os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(modules_path)

from Modules import recieve_email as rcmail
from Modules import send_email as sdmail

config_path = os.path.dirname(__file__) + "\config.ini"
print(config_path)

reciever = []
cf = configparser.ConfigParser()
cf.read(config_path)

email = cf.get("account","name")
password = cf.get("account","password")
pop3_server = 'pop.163.com'

if __name__ == "__main__":
    import time
    while(True):
        time.sleep(5)
        tmp_content = ""
        tmp_reciever = ""
        mail_server = rcmail.RecieveEmail(email, password, pop3_server)
        if mail_server.getMailNum() > 0:
            tmp_content = mail_server.getMailContent(1)
            tmp_reciever = mail_server.getMailFrom(1)
            while mail_server.getMailNum() != 0:
                mail_server.delMail(1)
            mail_server.loginOut()
            if tmp_content != "None":
                if  tmp_content.find("帮助") != -1:
                    mail_send = sdmail.SendEmail(email, password, sdmail.SMTPServe.dict['163'])
                    mail_send.setSender(email)
                    reciever.clear()
                    reciever.append(tmp_reciever)
                    mail_send.setReciever(reciever)
                    mail_send.setSubject("帮助")
                    func_num = int(cf.get("func","num"))
                    for i in range(1,func_num+1):
                        mail_send.addPlainContent(cf.get("func","func"+str(i))+"\n")
                    mail_send.sendEmail()
                elif tmp_content.find("1") != -1:
                    os.system("python E:\code\python\py-FundOnline\py_Email-fund.py")        
                elif tmp_content != None:
                    mail_send = Email(email, password, SMTPServe.dict['163'])
                    mail_send.setSender(email)
                    reciever.clear()
                    reciever.append(mail_server.getMailFrom(1))
                    mail_send.setReciever(reciever)
                    mail_send.setSubject("未知指令")
                    mail_send.addPlainContent("未知指令")
                    mail_send.sendEmail()
                    mail_server.delMail(1)







