import smptplib

sender_email = "xxxx@gmail.com"
password = "xxxabc"

sm = smtplib.SMTP("smtp.gmail.com", 587)

sm.login(gmail, password)

message = "Enter your message you want to send"

sm.sendmail(gmail, receiver_mail, message)

sm.quit()
