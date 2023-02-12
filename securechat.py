
def main():

    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. List all registered users")
    print("5. exit")
    number = input()
    username = set()
    available_nums = {'1', '2', '3', '4', '5'}
    while number not in available_nums:
        print("Please enter a number which corresponds to a function. ")
    while number in available_nums:
        while available_nums != '5':
            if available_nums == '1':
                def create_user():
                    print("Please input your name below: ")
                    input = input(': ')
                    print("You have selected " + available_nums + " press enter to exit.")
                if __name__ == '__main__':
                    create_user()
        while username in input:
            print("User already registered enter another name")
            input = input(': ')
            username.add(input)
            print("Username " + input + " registered")
        if __name__ == '__main__':
            create_user()
        while available_nums == '4':
            def list_reg_users():
                for user in username:
                    print(user)
                    print("You have selected " + available_nums + " press enter to exit.")
                    if __name__ == '__main__':
                        list_reg_users()
        leave_prog = input('')
if __name__ == '__main__':
    main()



