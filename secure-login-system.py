import hashlib
import os

USER_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    hashed = hash_password(password)

    with open(USER_FILE, "a") as f:
        f.write(username + "," + hashed + "\n")

    print("✅ Registration Successful!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)

    if not os.path.exists(USER_FILE):
        print("No users registered yet.")
        return

    with open(USER_FILE, "r") as f:
        users = f.readlines()

    for user in users:
        stored_username, stored_hash = user.strip().split(",")
        if username == stored_username and hashed == stored_hash:
            print("✅ Login Successful!")
            return

    print("❌ Invalid Credentials")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")