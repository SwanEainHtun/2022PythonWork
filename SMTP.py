import smtplib
sm = "swaneainhtun1212@gmail.com"
rm = ['Juanyswan6@gmail.com']
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sm,rm)
try:
    pw = input("enter Password");
    smtpObj = smtplib.SMTP("gmail.com",587)
    smtpobj.login(sm,pw)
    smtpObj.sendmail(sm,rm,message)
    print("Successfully sent mail.")
except Exception:
    print("Error:Unable to send an email.")