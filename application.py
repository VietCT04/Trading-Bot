from usermanager import User
from servicemanager import *
from tradingusermanager import TradingUser

class Application:
    
    def __init__(self):
        self.current_user = User()
    
    def login(self):
        print("\n=== Login ===")
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if User.authenticate(username, password):
                self.current_user = username
                print(f"Login successful! Welcome, {username}.")
                return True
            else:
                print("Invalid username or password. Please try again.")
                break
    
    def sign_up(self):
        print("\n=== Sign Up ===")
        while True:
            print("Choose the type of user to sign up:")
            print("1. Regular User")
            print("2. Trading User")
            user_type = input("Enter your choice (1 or 2): ").strip()

            if user_type not in {"1", "2"}:
                print("Invalid choice. Please choose 1 or 2.")
                continue

            username = input("Choose a username: ").strip()
            if username in User.credentials:
                print("Username already exists. Please try a different username.")
                continue

            password = input("Choose a password: ").strip()

            if user_type == "2":
                apikey = input("Enter your API key: ").strip()
                secretkey = input("Enter your secret key: ").strip()
                new_user = TradingUser.sign_up(username, password, apikey, secretkey)
            else:
                new_user = User.sign_up(username, password)

            if new_user:
                print(f"Sign-up successful! You can now log in as '{username}'.")
                return
            else:
                print("Failed to sign up. Please try again.")


    def show_menu(self):
        service_manager = ServiceManager()
        print("Choose a service (1-5):")
        user_choice = int(input()) 

        service_manager.choose_service(user_choice)

    def run(self):
        while True:
            print("\n=== Welcome ===")
            print("1. Login")
            print("2. Sign Up")
            print("0. Exit")

            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    if self.login():
                        self.show_menu()
                elif choice == 2:
                    self.sign_up()
                elif choice == 0:
                    print("Exiting the application. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a valid number.")
