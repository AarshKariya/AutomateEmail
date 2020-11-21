import pandas as pd 
import smtplib

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("example-email@gmail.com", "example-password")
msg = "How are you?"
subject = "Hey There!"
body = "Subject: {}\n\n{}".format(subject,msg)

for email in emails:
    server.sendmail("example-email@gmail.com", email, body)
server.quit()
