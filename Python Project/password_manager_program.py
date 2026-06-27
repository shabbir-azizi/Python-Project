import random
import string

paswords ={

}

# load exiting password 
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, passwords = line.strip().split(":")
            passwords [website] = passwords
except:
    pass 

def generate_password():
    chars=string.ascii_letters + string.digits + "!@#$%^&*()-+="
    password = "".join(random.choice(chars) for _ in range(12))
    return password

while True:
    print("\n----- PERSNOL PASSWORD MANAGER APP-----")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        