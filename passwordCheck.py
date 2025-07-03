import string
password = ()

def set_password(pw):
    global password
    if any(char.isalpha() for char in pw) and any(char.isdigit() for char in pw) and any(char in string.punctuation for char in pw):
        password = password + (pw,)
        print("Password added")
    
    else:
        print("Not Valid Password")    

def check_password(pw):
    if pw in password:
        print("Password is Valid")
    else:
        print("Password is not Valid")

        
set_pw = input("Your new Password:  ")
set_password(set_pw)
check_pw = input("Your valid Password:   ")
check_password(check_pw)