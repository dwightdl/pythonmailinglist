import smtplib
from logininfo import *

s = smtplib.SMTP()

s.connect('email-smtp.us-west-2.amazonaws.com', 587)

s.starttls()

#username and password
s.login(username, password)
