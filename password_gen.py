#Python password generator 
# 1) Import secrets, string, random to program for assistance to randomly choose among variables

import secrets
import string
import random

#Define password selection lists (abc, numbers, special characters and concatenate to a single string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
selection_list = letters + digits + special_chars

#Select length of password (set to eight for now/change for preferences)

password_len = str(input("How long do you want your password to be? (integers only) "))

#Initialize password string as empty.  
# Use for loop with range of password length defined as above to add characters to password 
# single quotations in loop to ensure no whitespace between characters

while True:
    password = ''
    for i in range (int(password_len)):
        password  += ''.join(secrets.choice(selection_list))
    if (any(char in special_chars for char in password) and sum (char in digits for char in password) >= 2):
        break

print(password)

print(password)
