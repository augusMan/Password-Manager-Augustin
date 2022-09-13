# Add New Credentials Function.

#This is a simple introduction 
print("\nHow to encrypt user detail...\n")

menu = """
Create a text file for credential storage if a text file does not already exist\n
Append new records to the text file without overwriting previous entries\n
"""
print("\n", menu, "\n")

#get user name
name = input ("Enter your name here: ")

# to encrypte the user password
password = input("Enter your password here: ")
charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
enpassword = "".join([charSet[(charSet.find(c)+3)%95] for c in password])
print("\nYour encrypted password is", enpassword)

website = input("Enter your URL here: ")

f = open("file.txt", "a")
f.write(name + "   " + enpassword + "   " + website + "   ")
print("\nYour new details have now been stored. ")
