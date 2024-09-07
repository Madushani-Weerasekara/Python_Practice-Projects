from cryptography.fernet import Fernet # allow to encrypt text

def load_key():
    file = open("key.key", "rb") # opening the file in read in bites mode
    key = file.read() # read the file
    file.close() # closing the file
    return key # returning the key
    
master_pwd = input("What is your master password? ")
key = load_key().master_pwd.encode() # convert master_pwd into bites and add it to the key
fer = Fernet(key) 

# Initializing a encryption module module
# key + password + text to encrypt = random text
# rendom text + key + password = text to encrypt

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # wb->write in bites mode
        key_file.write(key)
write_key()
"""


def view():
    with open('passwords.txt', 'r') as f: # r-> read mode
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User", user, "Password", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f: # a-> add
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n") # Taking the password turning into bytes with dot encode function and encrypting it. And converting the whole thin into string. And store it beside the name.



while True:
    mode = input("Would you like to add a new password or view existing one (view/add)?, or press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
        break

    elif mode == "add":
        add()
        


    else:
        print("Invalid mode.")
        continue