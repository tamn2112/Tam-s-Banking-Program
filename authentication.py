# User Registration Authentication
import hashlib
import json

# Open file 
try:
    with open('database.txt', 'r') as file:
        data = json.load(file)      
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data = []

def is_good_password(password: str):
    isLength = len(password) >= 8
    contain_one_digit = any(char.isdigit() for char in password)
    contain_one_lower_case = any(char.islower() for char in password)
    contain_one_upper_case = any(char.isupper() for char in password)
    contain_symbols = any(char in "!@#" for char in password)

    return isLength, contain_one_digit, contain_one_lower_case, contain_one_upper_case, contain_symbols

def is_good_username(username: str):
    return len(username) >= 3

def get_valid_username():
    username = input("Please create your username (more than 3 characters): ")
    while username in data:
        print("Username is already exist. Please choose a different one.")
        username = input("Please create your username (more than 3 characters): ")
    while not is_good_username(username):
        print("Invalid username, please try again.")
        username = input("Please create your username (more than 3 characters): ")
    return username

def get_valid_password():
    while True:
        password = input("Please create your password (contain at least: 8 characters, 1 digit, 1 lowercase, 1 uppercase, 1 special character): ")
        if all(is_good_password(password)):
            break
        print("Invalid password. Please try again.")

    return password

def registration():
    username = get_valid_username()
    password = get_valid_password()
    confirmed_password = input("Please confirm your password: ")
    while confirmed_password != password:
        print("Passwords don't match, please try again!")
        password = get_valid_password()
        confirmed_password = input("Please confirm your password: ")
    
    # Successfully get the final password!
    if confirmed_password == password:
        encode_password = confirmed_password.encode()
        hash_password = hashlib.sha256(encode_password).hexdigest()
    
    # put the username and password into data.json
    with open('database.txt', 'a') as file:
        json.dump({username: hash_password}, file)
        file.write('\n')
    return "Registration successful"









    
    


    

