
def main():
    username = set()
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. List all registered users")
    print("5. exit")
    number = input()
    available_nums = {'1', '2', '3', '4', '5'}
    while number not in available_nums:
        print("1. Create a user")
        print("2. Login")
        print("3. Connect to the chat")
        print("4. List all registered users")
        print("5. exit")
        while available_nums != '5':
            def create_user():
                print("Please input your name below: ")
                input = input(': ')
                while username in input:
                    print("User already registered enter another below")
                    input = input(': ')


if __name__ == '__main__':
    main()



