import smtplib

sender_email = "xxxx@gmail.com"
password = "xxxabc"

receiver_mail = "xyz123@gail.com"

try:
    sm = smtplib.SMTP("smtp.gmail.com", 587)
    sm.starttls()
    sm.login(sender_email, password)
    
    subject = "Subject: Test Email\n"
    body = "Enter your message you want to send"
    message = subject + body
    sm.sendmail(sender_email, receiver_mail, message)
    print ("Email Sent Succesfully!")

except Exception as e:
    print (f"An Error Occured: {e}")

finally:
    sm.quit()
