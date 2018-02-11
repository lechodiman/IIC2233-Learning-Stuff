import smtplib
password = ''

content = 'example email stuff here, blabla this is an email ctm'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('luis.shodyman@gmail.com', password)

mail.sendmail('luis.shodyman@gmail.com', 'luis.shodyman@gmail.com', content)

mail.close()
