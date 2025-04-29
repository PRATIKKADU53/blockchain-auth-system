from user_auth import AuthSystem

def main():
    auth = AuthSystem()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            auth.register_user(uname, pwd)

        elif choice == "2":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            auth.login_user(uname, pwd)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
