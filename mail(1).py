import smtplib

content = 'hello'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('kushdarji1110@gmail.com','Kush@1198')

mail.sendmail('kushdarji1110@gmail.com','kushdarji11@gmail.com',content)

mail.close()

