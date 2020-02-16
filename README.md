email
=====

Simple email modules for Python

### Purpose
The ```email``` modules is designed to be simple to use, no need to typing a lot of codes to run your own email items.

The ```email``` Module currently supports the following:
*  From, To, and Cc fields
*  Text and HTML Message Body
*  Attachments
*  Read Receipts
*  Custom headers
*  More to come!

### Examples
#### Sending email using 163
```python
email = Email('***@163.com', '****', SMTPServe.dict['163'])
email.setSender('****@163.com')
email.setReciever(['****@qq.com'])
email.setSubject("test for send email")
email.addPlainContent("this is a attachment")
email.sendEmail()
```

#### Attaching a File
```python
email = Email('***@163.com', 'password', SMTPServe.dict['163'])
email.setSender('****@163.com')
email.setReciever(['****@qq.com'])
email.setSubject("test for send email")
email.addAttachFile("xxxx.rar")
email.sendEmail()
```

#### Recieving email using 163
```python
email = rcmail.RecieveEmail('***@163.com', 'password', "pop.163.com")
if email.getMailNum() > 0:
    tmp_content = email.getMailContent(1)
    tmp_reciever = email.getMailFrom(1)
    while email.getMailNum() != 0:
        email.delMail(1)
    email.loginOut()
```


