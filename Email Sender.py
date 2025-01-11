import smtplib

while True:
    sender_email = input("Enter your email: ")
    password = input("Enter your password: ")
    receiver_email = input("Enter the recipient's email address: ")
    subject_input = input("What is the subject of your email? ")
    body_input = input("What is the message? ")

    subject = f"Subject: {subject_input}\n"
    try:
        sm = smtplib.SMTP("smtp.gmail.com", 587)
        sm.starttls()
        sm.login(sender_email, password)
        message = subject + body_input
        sm.sendmail(sender_email, receiver_email, message)
        print ("Email Sent Succesfully!")
    except Exception as e:
        print (f"An Error Occured: {e}")
    finally:
        sm.quit()

    send_again = input("Do you want to send again (y/n)?: ")
    if send_again != 'y':
        print ("Thanks for using")
        break
