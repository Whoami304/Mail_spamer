import smtplib
from email.mime.text import MIMEText
import pyglet
import tqdm
from colorama import Fore, Back, Style
from colorama import init
init()

def Fuck_up_mail(sender,mail_adr,passwd,text,subject):

     
    

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    try:
      server.login(sender, passwd) 
      
     
      Send_it = MIMEText(text)

      Send_it["from"] = sender
      Send_it["to"] = mail_adr
      Send_it["subject"] = subject
      
    
      server.sendmail(sender, mail_adr,Send_it.as_string())
      
      print(Fore.RED)
      
      return f"spaming {mail_adr}...".strip()
       
    
    except Exception as Spam_send_Error:
           return f"spam was not sent{Spam_send_Error}"


