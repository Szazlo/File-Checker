import hashlib
import time
import smtplib, ssl
from datetime import datetime

#todo
    #update hash after change dections
    #overwrite file string method

#Start loop
while True:
    hashing = hashlib.md5()

    #File to check goes into open
    with open('FILE_GOES_HERE', 'rb') as afile:
        buf = afile.read()
        hashing.update(buf)
        #Define "a" as MD5 check of original file 
        origin = "ORIGIN_HASH_GOES_HERE"
        checksum = hashing.hexdigest()
        success = "Checksum is the same"
        failure = "Discrepancy detected in checksum, sending email!"

    #Get current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        #if sum is same
        if origin == checksum :
            print(success, "-", current_time)
            time.sleep(10)
            continue
        else: 
         print(failure, "-", current_time)
         #email config
         smtp_server = 'smtp.gmail.com'
        port = 465

        sender = 'sample@gmail.com'
        password = 'samplepassword'

        context = ssl.create_default_context()

        receiver = 'receiver@gmail.com'
        
        #get content of hash file
        with open('jcodes.json') as f:
            contents = f.read()

            message = (contents)

            #sends email
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender, password)
                #Sending email
                server.sendmail(sender, receiver, message)
                print("Email Sent! -", current_time)
                break