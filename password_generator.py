
import random
import string 
length = int(input("Enter password length:"))
characters= string.ascii_letters + string.digits +"!@#$%^&*"
password = ""
for _ in range(length):
    password += random.choice(characters) 
print("/ngenerated password:")
print(password)
if length < 9:
        print("strength:weak")
elif length <12:
        print("strength:medium")
else:
        print("strength:strong")
        