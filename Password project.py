from cryptography.fernet import Fernet 

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password?")
key = load_key + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("password.text", "r") as f:
        for line in f.redlines():
            data = (line.rstrip())
            user, passw, phonenum = data.split("|")
            print("User:", user, "Password:", fer.decrypt(passw.decode())), "Phone:", phonenum)

def add():
    name = input("Account name?")
    pwd = input("Password:")
    phone = input("Phone number:")

    with open("password.text", "a") as f:
        f.write(name + "" + fer.encrypt(pwd.encode())) + "|" + phone + "/n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit.").lower
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue
