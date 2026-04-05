''' needs:
Twilio : gives facility to connect with wtsp API, iska client class directly msg send krne ke kaam ayega : single line of code & msg send
datetime module : used to calculate diff between needed & current time
time module : time me send krna h
'''

# step-1 install required libraries
from twilio.rest import Client  #client class import so wtsp msg send krne kaam ayega
from datetime import datetime, timedelta    #timedlt: to clclt time diff
import time

# step-2 twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
# account_sid & auth_tokem - twilio API authenticate krne k liye use hote h
client = Client(account_sid, auth_token)

# step-3 design send msg function
def send_wtsp_msg(recipient_number, message_body, name):
    try:
        message = client.messages.create(
            from_ = 'whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f"message sent successfully to {name}")
        #print(f"message sent successfully, message SID{message.sid}")
    except Exception as e:
        print("debugged API errors by  Twilio sandbox authentication issues.", e)

# step-4 User input
name = input("enter the recipent name : ")
recipient_number = input("Enter recipent number with country code (eg. +91) : ")
message_body = input(f"Enter message you want to send to {name} : ")

# step-5 parse date/time & calculate delay
date_str = input("Enter the date you want to send message (DD-MM-YYYY) : ")
time_str = input("Enter the time you want to send message (HH:MM 24hrs format) : ")
# datetime module - fetch current date time,  no. ko date time format me convert, diff btw current & need date
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%d-%m-%Y %H:%M")
# strp kyuki python text me input lega, usko datetime object me cnvrt yhi krega
current_datetime = datetime.now()

# calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds<=0:
    print("the specified time is in the past, please enter future date & time.")
else:
    print(f"message scheduled to be sent to {name} at {schedule_datetime}.")
    # wait until the scheduled time
    time.sleep(delay_seconds)
    # send message
    send_wtsp_msg(recipient_number, message_body, name)