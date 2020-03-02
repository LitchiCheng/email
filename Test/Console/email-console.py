
import os,configparser,sys

modules_path = (os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(modules_path)
from Modules import recieve_email as rcmail
from Modules import send_email as sdmail
import config_tool as ct

config_path = os.path.dirname(__file__) + "\config.ini"
cf = configparser.ConfigParser()
cf.read(config_path)

reciever = []
email = cf.get("account","name")
password = cf.get("account","password")
pop3_server = 'pop.163.com'
freq = int(cf.get("frequency","time"))
last_content=""

if __name__ == "__main__":
    import time
    mail_server = rcmail.RecieveEmail(email, password, pop3_server)
    mail_send = sdmail.SendEmail(email, password, sdmail.SMTPServe.dict['163'])
    while(True):
        if not mail_server.loginStatus():
            print("login failed")
            time.sleep(60)
            mail_server.loginIn()
            continue
        if mail_server.getMailNum() > 0:
            tmp_content = mail_server.getMailContent(mail_server.getMailNum())
            print(tmp_content)
            print(mail_server.getMailNum())
            if str(last_content) == str(tmp_content):
                continue
            last_content = tmp_content

            tmp_reciever = mail_server.getMailFrom(mail_server.getMailNum())
            if tmp_content != "None":
                if  tmp_content.find("帮助") != -1:
                    mail_send.setSender(email)
                    reciever.clear()
                    reciever.append(tmp_reciever)
                    mail_send.setReciever(reciever)
                    mail_send.setSubject("帮助")
                    func_num = int(cf.get("func_list","num"))
                    for i in range(1,func_num+1):
                        mail_send.addPlainContent(cf.get("func_list","func"+str(i))+"\n")
                    mail_send.sendEmail()
                elif tmp_content[0] == "1":
                    print("111111")
                    os.system(cf.get("func_cmd","func1"))
                elif tmp_content[0] == "2":
                    print("22222")
                    print(tmp_content.lstrip("2+"))
                    ct.addFund(tmp_content.lstrip("2+"))
                elif tmp_content[0] == "3":
                    print("33333")
                    print(tmp_content.lstrip("3+"))
                    ct.delFund(tmp_content.lstrip("3+"))       
                elif tmp_content != None:
                    mail_send.setSender(email)
                    reciever.clear()
                    reciever.append(mail_server.getMailFrom(mail_server.getMailNum()))
                    mail_send.setReciever(reciever)
                    mail_send.setSubject("未知指令")
                    mail_send.addPlainContent("未知指令")
                    mail_send.sendEmail()
        mail_server.loginOut()
        time.sleep(10)







