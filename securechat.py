
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
        print("1. Create a user")
        print("2. Login")
        print("3. Connect to the chat")
        print("4. List all registered users")
        print("5. exit")
        print("Please print one of the numbers")
        number = input()
    while number != '5':
        if number == '1':
            # noinspection PyTypeChecker
            def create_user():
                print("Please input your name below: ")
                name = input(': ')
                if name in username:
                    print("User already registered enter another name")
                else:
                    username.add(input)
                    print("Username " + name + " registered")
                    print("Press enter to go back.")
                    l = input()
                    breakpoint()
            create_user()
        if number == '4':
            def list_reg_users():
                for user in username:
                    print(user)
                    print("You have selected " + available_nums + " press enter to exit.")
                    l = input()
                    break
            list_reg_users()
    leave_prog = input('')
if __name__ == '__main__':
    main()



