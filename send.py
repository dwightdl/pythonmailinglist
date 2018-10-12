import smtplib
from logininfo import username, password

s = smtplib.SMTP()

s.connect('email-smtp.us-west-2.amazonaws.com', 587)

s.starttls()

#username and password
s.login(username, password)

msg = 'From: sbb.david@gmail.com\nTo: david@submetersolutions.com\nSubject: Test email\n\n%s' % body

body = 'This is a test email'

s.sendmail('sbb.david@gmail.com', 'david@submetersolutions.com', msg)
