import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logininfo import username, password

class AWSSender:

	s = smtplib.SMTP()

	s.connect('email-smtp.us-west-2.amazonaws.com', 587)

	s.starttls()

	#username and password
	s.login(username, password)

	def quit(self):
		s.quit()

	def send(self, email, me):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Hello World!"
		msg['From'] = me
		msg['To'] = email

		# Create the body of the message (plain text and an HTML version)
		text = "Email send using a template!"
		html = open('template.html', 'r').read()

		html = html.replace('{{ content }}', text)

		# Record the MIME types of both parts - text/plain and text/html
		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		# Attach parts into message container
		msg.attach(part1)
		msg.attach(part2)

		self.s.sendmail(me, email, msg.as_string())
		print("Sent email to " + email, end="")

emaillist = open('list.txt', 'r').readlines()

aws = AWSSender()

for email in emaillist:
	aws.send(email, "sbb.david@gmail.com")

