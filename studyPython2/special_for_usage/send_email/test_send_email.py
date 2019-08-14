#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class TestSendEmail(object):

    def test_send_email(self):
        # 设置服务器所需信息
        # 邮箱服务器地址
        mail_host = 'smtp.qq.com'
        # 用户名
        mail_user = '1205161876@qq.com'
        # 密码(部分邮箱为授权码)：qq授权码：iqmqqmartllefgff
        mail_pass = 'iqmqqmartllefgff'
        sender = '1205161876@qq.com'
        receivers = ['fairy.li@bytecenture.com']

        #设置email信息
        # 邮件内容设置
        message = MIMEText('content', 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = Header('Just For Test', 'utf-8')  # 邮件主题
        # 发送方信息
        message['From'] = sender
        # 接受方信息
        message['To'] = receivers[0]
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 465)

            smtpObj.ehlo()
            smtpObj.starttls()
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            # 退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误
