import random
import string
from manager import PasswordManager
from generator import PasswordGenerator

def main():
    password_manager = PasswordManager()
    password_generator = PasswordGenerator()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. Generate Password")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            site = input("Enter the site name: ")
            password = input("Enter the password: ")
            password_manager.add_password(site, password)
            print(f"Password for {site} added.")
        
        elif choice == '2':
            site = input("Enter the site name: ")
            password = password_manager.retrieve_password(site)
            if password:
                print(f"Password for {site}: {password}")
            else:
                print(f"No password found for {site}.")
        
        elif choice == '3':
            site = input("Enter the site name: ")
            password_manager.delete_password(site)
            print(f"Password for {site} deleted.")
        
        elif choice == '4':
            length = int(input("Enter the desired password length: "))
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            new_password = password_generator.generate_password(length, include_symbols, include_numbers)
            print(f"Generated Password: {new_password}")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()