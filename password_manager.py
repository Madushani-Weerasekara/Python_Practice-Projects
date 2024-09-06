master_pwd = input("What is your master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
            break

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


mode = input("Would you like to add a new password or view existing one (view/add)?, or press q to quit ").lower()
while True:
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue