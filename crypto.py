import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
from dhooks import Webhook
import bs4
import time
import json
import os
from email.message import EmailMessage
import ssl
import smtplib
import getpass

i = input("Enter the name of crypto currency you want to get notified for - ")
platform = input("On which of the platform you want to get notiified on- \n 1. Discord \n 2. Email \n 3. Both \n (Note - Please enter number only)\n")
time_interval = input("After what time you want to get notified. (In seconds) -- ")
sender = input('Enter your email -- ')
password = getpass.getpass('Enter your password -- ')
password_length = len(password)
password_hide = ('*' * password_length)
reciever = input("Enter email address you want to send mail to -- ")

while True:
  url = 'https://api.coincap.io/v2/rates/'+i
  headers = {
              'Accepts': 'application/json',
  }
  session = Session()
  session.headers.update(headers)

  response = session.get(url)
  data = json.loads(response.text)
  crypto=float((data['data']['rateUsd']))

  if platform == "1":
    hook = Webhook("https://discord.com/api/webhooks/1003993992360366080/1cS8w3N2GHzW-2aAwLYZ9tpfcHHhRBiASgTIafnfJ1Q--NbC1Exat7lVVzr4mgvH3l5f")
    hook.send(f"Current price of {i} is = {round(crypto, 2)} Indian Rupees")

  elif platform == "2":
    subject = "UPDATE - Current price of "+ i
    body = f"Hello from tell.it \n Current price of {i} is = {round(crypto, 2)} Rupees"

    em = EmailMessage()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    port_number = 465
    with smtplib.SMTP_SSL("smtp.gmail.com", port_number, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())
  
  elif platform == "3":
    hook = Webhook("https://discord.com/api/webhooks/1003993992360366080/1cS8w3N2GHzW-2aAwLYZ9tpfcHHhRBiASgTIafnfJ1Q--NbC1Exat7lVVzr4mgvH3l5f")
    hook.send(f"Current price of {i} is = {round(crypto, 2)} Indian Rupees")

    subject = "UPDATE - Current price of ", i
    body = f"Hello from tell.it \n Current price of {i} is = {round(crypto, 2)} Rupees"

    em = EmailMessage()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    port_number = 465
    with smtplib.SMTP_SSL("smtp.gmail.com", port_number, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())

  else:
    print("Please enter the correct value")
  
  time.sleep(int(time_interval))