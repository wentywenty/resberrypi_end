# 发送邮件
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

sender = '2904017884@qq.com'  # 发件人邮箱
receiver = '2806900184@qq.com'  # 收件人邮箱
mail_pass = 'kvvqtlszxapnddgb'  # qq邮箱授权码

message = MIMEMultipart()

# 添加Header信息，From，To，Subject分别为发送者信息，接收者消息和邮件主题
message['From'] = formataddr((str(Header('发件人', 'utf-8')), sender))
message['To'] = formataddr((str(Header('收件人', 'utf-8')), receiver))

subject = 'aa'
message['Subject'] = Header('有陌生人试图开门！！！', 'utf-8')

try:
    smtpObj = smtplib.SMTP('smtp.qq.com', 25)  # smtp.xxx.com为邮箱服务类型，25为STMP
    smtpObj.login(sender, mail_pass)  # 登录
    smtpObj.sendmail(sender, receiver, message.as_string())  # 发送
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 邮件发送失败")
