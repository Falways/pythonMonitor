#!/usr/bin/python3
import time,sched
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1914783590@qq.com'  # 发件人邮箱账号
my_pass = 'xbsdrzbnlzoqbfhc'  # 发件人邮箱密码
to_user = ['1914783590@qq.com','15971362697@139.com']  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('系统出现XX错误，请尽快处理哦！', 'plain', 'utf-8')
        msg['From'] = formataddr(["xuhang", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(to_user)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "系统故障检查通知"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, to_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")