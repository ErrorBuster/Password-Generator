import hashlib
import getpass

password_manager = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(service, username, password):
    password_manager[service] = (username, hash_password(password))
    print(f"Password for {service} has been added.")

def get_password(service):
    try:
        username, hashed_password = password_manager[service]
        password = getpass.getpass(f"Enter password for {service}: ")
        if hash_password(password) == hashed_password:
            print(f"Username for {service}: {username}")
            print(f"Password for {service}: {password}")
        else:
            print("Incorrect password.")
    except KeyError:
        print(f"Password for {service} not found.")

while True:
    print("1. Add password")
    print("2. Get password")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        service = input("Enter service name: ")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        add_password(service, username, password)
    elif choice == 2:
        service = input("Enter service name: ")
        get_password(service)
    else:
        break
