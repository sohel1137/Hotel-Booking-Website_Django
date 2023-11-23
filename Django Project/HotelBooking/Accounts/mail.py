from email.message import EmailMessage
import random
import ssl
import smtplib
from django.shortcuts import render
#_______________________OTP generator and varification___________________________
def send_mail(reciver_mail,username,start_date,end_date,ROOM_TYPES,booking_type):
    e_send="Your Email"
    e_pass="Your Password"
    e_reci=reciver_mail
   

    sub=" BOOKING CONFIRAMATION "
    body=f''' PARADISE HOTEL 

Dear {username},
We are delighted to confirm your booking with us at Hotel ! Your reservation has been successfully secured.

Booking Details:
Check-in Date: {start_date} 
Check-out Date: {end_date}
payemnt Gatway: {ROOM_TYPES}
Room/Service Booking Type:{booking_type}

If your plans change or if you need to make any adjustments to your booking, please inform us at your earliest convenience.
Thank you once again for choosing ParadiseHotel.com. We are eagerly anticipating your arrival and are dedicated to providing you with an outstanding experience.

Warm regards,

ParadiseHotel.com
contact-12345 67890



'''

    es=EmailMessage()

    es['FROM']=e_send
    es['TO']=e_reci
    es['SUBJECT']=sub

    es.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
        smtp.login(e_send,e_pass)
        smtp.sendmail(e_send,e_reci,es.as_string())
    
    data=[e_reci]

    return data



#_______________________OTP generator and varification___________________________
def send_CancelMail(reciver_mail,username,start_date,end_date,ROOM_TYPES,booking_type):
    e_send="sohelshaikh9583@gmail.com"
    e_pass="imijgunvtnwurcxh"
    e_reci=reciver_mail
   

    sub=" Booking Cancellation "
    body=f''' PARADISE HOTEL 
'
Dear {username},

Your Booking Cancel Succsfully...!

Booking Details:
Check-in Date: {start_date} 
Check-out Date: {end_date}
payemnt Gatway: {ROOM_TYPES}
Room/Service Booking Type:{booking_type}
Total Cost: {Ammount}


Warm regards,

ParadiseHotel.com
contact-12345 67890



'''

    es=EmailMessage()

    es['FROM']=e_send
    es['TO']=e_reci
    es['SUBJECT']=sub

    es.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
        smtp.login(e_send,e_pass)
        smtp.sendmail(e_send,e_reci,es.as_string())
    
    data=[e_reci]

    return data