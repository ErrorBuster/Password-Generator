import random
import string

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

length = int(input("Enter the desired password length: "))
print("Your generated password is:", generate_password(length))
