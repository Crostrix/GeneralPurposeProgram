import win32com.shell.shell
import os
import base64
import string
import secrets
import pyshorteners

letters = string.ascii_letters
digits = string.digits
Special = string.punctuation

alfabeth = letters + digits + Special

commands = ''
question = "Welcome!\n[B] Base64 Encode/Decode\n[A] Account control center\n[P] Password Generator\n[C] Computer control\n[S] URL Shortener\n[Q] Quit\n\nWhat want you to do? "
accountMode = "Which account is gonna change?"
base64mode = ""
mark = '"'
pwd = ""
pwd_len = 12
Computer_Management_Question2 = "Welcome to computer control\n[C] Control panel\n[R] Registry editor\n[S] Shutdown\n[M] Setting Menu\nWhat will it be? "

os.system("cls")
print("Welcome to the multiple use program!\n")
mode = input(question)

while 1 == 1:
    if ((mode == "B") or (mode == "b")):
       os.system("cls")
       print("Welcome to the base64 section\n")
       base64mode = input("[E] Encode\n[D] Decode\n\nWhat will it be? ")
    if ((base64mode == "E") or (base64mode == "e")):
        os.system("cls")
        encodingmessage = input("What will the message be to be encoded? ")
        encodingmessage_bytes = encodingmessage.encode("ascii")
        base64_bytes = base64.b64encode(encodingmessage_bytes)
        base64_message = base64_bytes.decode("ascii")
        print(base64_message)
        os.system("pause")
        os.system("cls")
        mode = input(question)

    if ((base64mode == "D") or (base64mode == "d")):
        os.system("cls")
        decodingmessage = input("What will the message be to be decoded? ")
        decodingmessage_bytes = decodingmessage.encode("ascii")
        base64_decodedmessage = base64.b64decode(decodingmessage_bytes)
        base64_decodedmessage_bytes = base64_decodedmessage.decode("ascii")
        print(base64_decodedmessage_bytes)
        os.system("pause")
        os.system("cls")
        mode = input(question)

    if ((mode == "A") or (mode == "a")):
        os.system("cls")
        print("Administrator permission required!!")
        AccountQuestion = input("What to you want to do\n[C] Change someones password\n[M] Make an account\n[D] Delete an account\n[A] Make a account administrator\nWhat do you want to do? ")
        if ((AccountQuestion == "C") or (AccountQuestion == "c")):
            accountchangequestion = input(accountMode)
            passwordQuestion = input("What will the new password be")
            commands = "net user " + mark + accountMode + mark + passwordQuestion
            win32com.shell.shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            commands = ''
            print("Operation successful")
            os.system("pause")
            os.system("cls")
            mode = input(question)
    
        if ((AccountQuestion == "M") or (AccountQuestion == "m")):
            os.system("cls")
            newaccount = input("What will be the new name of the account? ")
            commands = "net user " + mark + newaccount + mark + " /add"
            win32com.shell.shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            commands = ''
            print("Operation successful")
            os.system("pause")
            os.system("cls")
            mode = input(question)
    
        if ((AccountQuestion == "D") or (AccountQuestion == "d")):
            accountchangequestion = input(accountMode)
            commands = "net user " + mark + accountchangequestion + mark + " /del"
            win32com.shell.shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            print("Operation successful")
            os.system("pause")
            os.system("cls")
            mode = input(question)

        if ((AccountQuestion == "A") or (AccountQuestion == "a")):
            accountchangequestion = input(accountMode)
            commands = "net localgroup Administrators " + mark + accountchangequestion + mark +  " /add"
            win32com.shell.shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            os.system("pause")
            os.system("cls")
            mode = input(question)

    if ((mode == "Q") or (mode == "q")):
        print("Im quitting")
        exit()

    if ((mode == "P") or (mode == "p")):
        for i in range(pwd_len):
            pwd += ''.join(secrets.choice(alfabeth))
        print(pwd)
        os.system("pause")
        os.system("cls")
        mode = input(question)
    
    if ((mode == "C") or (mode == "c")):
        os.system("cls")
        Computer_Management_Question = input(Computer_Management_Question2)
        if ((Computer_Management_Question == "C") or (Computer_Management_Question == "c")):
            os.system("control")
            os.system("pause")
            os.system("cls")
            mode = input(question)

        if ((Computer_Management_Question == "M") or (Computer_Management_Question == "m")):
            os.system("start ms-settings:")
            os.system("pause")
            os.system("cls")
            mode = input(question)
        
        if ((Computer_Management_Question == "R") or (Computer_Management_Question == "r")):
            os.system("regedit")
            os.system("pause")
            os.system("cls")
            mode = input(question)

        if ((Computer_Management_Question == "S") or (Computer_Management_Question == "s")):
            os.system("shutdown -s -t 0")

        if ((Computer_Management_Question == "R") or (Computer_Management_Question == "r")):
            os.system("regedit")
            os.system("pause")
            os.system("cls")
            mode = input(question)
    
    if ((mode == "S") or (mode == "s")):
        longurl = input("Which url is gonna made shorter? ")
        shorturl_maker = pyshorteners.Shortener()
        shorturl = shorturl_maker.tinyurl.short(longurl)
        print(shorturl)
        os.system("pause")
        os.system("cls")
        mode = input(question)
