''' ----------note:----------
    -the code itself only 97 
    ----lines if we remove---
    --the comments and empty-
    ----------lines----------
    -I only did this to make-
    -the code more readable--
    -----and look better-----'''


import time as t
from cryptography.fernet import Fernet as F

# File paths
file_name = "PASSWORD MANAGER/data.txt"
key_file_name = "PASSWORD MANAGER/key.key"

# Master key (used for accessing the password manager :)
master_key = 123

# Load or generate encryption key
def load_or_generate_key():
    
    try:
        # Try to load the key from the file
    
        with open(key_file_name, "rb") as key_file:
            key = key_file.read()
    
    except FileNotFoundError:
        # If the key file does not exist, generate a new key
        key = F.generate_key()
        # Save the key to the file for future use
    
        with open(key_file_name, "wb") as key_file:
            key_file.write(key)
    
    return key

# Initialize cipher suite with the loaded key
key = load_or_generate_key()
cipher_suite = F(key)

# Encryption and decryption functions
def encrypt_password(password, cipher_suite):
    
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, cipher_suite):
    
    try:
        return cipher_suite.decrypt(encrypted_password.encode()).decode()
    
    except Exception as e:
        print(f"Failed to decrypt password: {e}")
        return None

def view():
    
    data = read_from_file()
    lines = data.splitlines()  # Split the data into individual lines
    
    print("Name🔽,   Password🔽")
    
    for line in lines:
    
        if line.strip():  # Skip empty lines
    
            name, encrypted_passw = line.split("|")  # Split each line into name and encrypted password
            decrypted_passw = decrypt_password(encrypted_passw, cipher_suite)
    
            if decrypted_passw:
    
                data_to_display = f"\n{name} | {decrypted_passw}"
                print(data_to_display)
# Function to write encrypted password data to file
def write_in_file(name, passw):
    
    passw = encrypt_password(passw, cipher_suite)
    with open(file_name, "a") as file:
    
        data_to_be_written = name + "|" + passw + "\n"
        file.write(data_to_be_written)

# Function to read encrypted password data from file
def read_from_file():
    
    with open(file_name, "r") as file:
    
        data = file.read()
        return data
    
def remove_password():
    
    view()
    
    service_name = input("Which password to remove : ")
    # Read all lines from the file
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    # Find the line to remove
    for line in lines:
    
        if line.startswith(service_name + "|"):
    
            lines.remove(line)
            break
    
    print("Here is an updated version of the data.")
    view()
    
    # Write the updated list of lines back to the file
    with open(file_name, "w") as file:
        file.writelines(lines)
# Function to display all stored passwords

# Function to add a new password
def add():
    
    name = input("Enter the name of the password: ")
    passw = input(f"Enter the password for {name}: ")
    write_in_file(name, passw)
    print("Here is an updated version of the data.")
    view()

# Secondary menu to choose between viewing, adding, or removing passwords
def secondary_main():
    
    choice = int(input("\n1. View\n2. Add\n3. Remove\n0. Exit\n\n:- "))
    
    if choice == 0:
        print("Bye.👋")
    
    elif choice == 1:
        view()
    
    elif choice == 2:
        add()
    
    elif choice == 3:
        remove_password()


def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Time remaining: {remaining} seconds", end='\r')
        t.sleep(1)
    print("You can try again now!    ")  # To clear the line after countdown

def primary_main():
    countdown_time = 60
    attempts_remaining = 3
    
    while attempts_remaining > 0:
        attempts_remaining -= 1
        entered_key = int(input("Please enter the master key: "))
    
        if entered_key == master_key:
            secondary_main()
            break
        else:
            print("Wrong key!")
    
        if attempts_remaining == 0:
            print("You have entered the wrong key too many times.")
            countdown_timer(countdown_time)

# The rest of your code would go here...

                
# Entry point of the program
if __name__ == "__main__":
    
    print("Welcome to the Password manager!\n")
    primary_main()