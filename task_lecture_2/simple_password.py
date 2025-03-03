import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def check_password(stored_hash, entered_password):
    return bcrypt.checkpw(entered_password.encode(), stored_hash)


users = {}
username = input("Enter username: ")
password = input("Enter password: ")

users[username] = hash_password(password)

print("User registered successfully!")

username = input("\nEnter username to login: ")
password = input("Enter password: ")

if username in users and check_password(users[username], password):
    print("Login successful!")
else:
    print("Invalid username or password.")
