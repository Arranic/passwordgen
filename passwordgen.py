#! python3
# creator: robert griffin
# modified: jonathan estep
import random,os,string

# Define the function that creates a new file
def out_file(filepath, new_passwords):
    try:
        with open(filepath, "w") as file:
            file.write("\n".join(str(item) for item in new_passwords))
    except:
        print("Unable to write to path")

def generate_password(password_length):
    # These are the characters we'll use to generate passwords from
    password = ''
    specials = ['!','@','$','%','^','&','*','<','>','?',';','~',]
    while len(password) < password_length:
        for i in range(2):
            password += random.choice(string.ascii_lowercase)
            password += random.choice(string.ascii_uppercase)
            password += random.choice(string.digits)
            password += random.choice(string.punctuation)
            password += random.choice(specials)
    list_password = list(password)
    random.shuffle(list_password)
    new_password = ''.join(list_password)
    return new_password

# Here is our main function!
def main():
    
    # Define the output file path
    filepath = "C:\Temp\passwords.txt"

    # Delete the previously existing file    
    if os.path.exists(filepath):
        os.remove(filepath)
    
    # Print the welcome
    print('\n====== Welcome to Griffin Password Gen 1.0 ======')

    # Get input from user on how many passwords to generate
    print('\nHow many passwords do you want to generate?')
    number = int(input())

    # Get input from user on how long the password needs to be
    print('How long does your password need to be?')
    password_length = int(input())

    passwords = []

    for i in range(number):
        passwords.append(generate_password(password_length))
        
    print(f"Here are your new passwords:")
    for i in passwords:
        print(i)
    
    # Create the new file for the passwords and add each password on its own line
    out_file(filepath, passwords)
    
    # Closing statements and good-byes
    print('\nYour passwords were saved to C:\Temp for your convenience.')

# Call the Main function!
if __name__ == '__main__':
    main()