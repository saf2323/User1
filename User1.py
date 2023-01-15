from getpass import getpass
import os

#inputs

user = input("ENTER USERNAME: ")
passwrd = getpass("ENTER PASSWORD: ")

#statment

if user=='Safdark' and passwrd=='1233':
    print('LOGGED')
    os.system('netsh')
else:
    print('LOGGED ERROR')