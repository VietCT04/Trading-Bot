from user import User
from service import Service

class Application:
    """Main application to handle login, sign-up, and service menu."""
    
    def __init__(self):
        self.current_user = None
    
    def login(self):
        """Manages the login process."""
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
    
    def sign_up(self):
        """Manages the sign-up process."""
        print("\n=== Sign Up ===")
        while True:
            username = input("Choose a username: ")
            if username in User.credentials:
                print("Username already exists. Please try a different username.")
                continue

            password = input("Choose a password: ")
            if User.sign_up(username, password):
                print(f"Sign-up successful! You can now log in as '{username}'.")
                return
            else:
                print("Failed to sign up. Please try again.")

    def show_menu(self):
        """Displays the service menu and handles user choices."""
        while True:
            print("\n=== Main Menu ===")
            print("1. Service 1")
            print("2. Service 2")
            print("3. Service 3")
            print("4. Service 4")
            print("5. Service 5")
            print("0. Logout")
            
            try:
                choice = int(input("Choose a service (1-5) or 0 to logout: "))
                if choice == 1:
                    Service.service_1()
                elif choice == 2:
                    Service.service_2()
                elif choice == 3:
                    Service.service_3()
                elif choice == 4:
                    Service.service_4()
                elif choice == 5:
                    Service.service_5()
                elif choice == 0:
                    print(f"Goodbye, {self.current_user}!")
                    self.current_user = None
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        """Runs the application."""
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