from mailspam import *
from colorama import Fore, Back, Style
from colorama import init
from getpass import getpass
from tqdm import tqdm
init()

def main():
    #sender,mail_adr,passwd,subject,text,
    try:

     with open('logo.txt') as f:
          print(f.read())
    except FileNotFoundError:
      raise("file can't found ")   
    
    print(Fore.RED)
    
    sender  = input("\nEnter mail :")
    mail_adr = input("Enter mail addresant :")
    password = getpass('Enter password :')
    subject = input("Enter  subject :")
   
    text = input("\nEnter Text :")
    
    print(Fore.GREEN)
    nums = int(input("\nHow many times do you want to send text ::")) 

    print("\nstarting... ") 
    for spam in tqdm(range(1,nums+1)):                
        print(Fuck_up_mail(sender,mail_adr,password,subject=subject,text=text),spam)
    print(Fore.GREEN)
    print("\nprogram closed")    
if __name__ == "__main__":
    main()
