#Random Password Generator

import random
import string
import secrets

def create_password(length):
    user_password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for random_password in range(int(length))))
    print("Your password is " + user_password+"\nKeep it secure and safe.\n")

def user_input():
    try:    
        user_len = int(input("Enter a length of your wanted password : ")) 
        create_password(user_len)

    except ValueError:
        print("Oops! That was not a valid number. Please Try Again\n")
        user_input()
        
user_input()



















