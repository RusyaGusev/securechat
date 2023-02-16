
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
            username_register(username)
        elif number == '4':
            list_all_user(username)
            print("1. Create a user")
            print("2. Login")
            print("3. Connect to the chat")
            print("4. List all registered users")
            print("5. exit")
            number = input()
    print("Thank you for using our secret chat!")
    quit()


def username_register(username):
    print("Please input your name below: ")
    name = input(': ')
    while name in username:
        print('Username already exists please enter another one')
        name = input(': ')
    username.add(name)
    print("Username " + username + " has been registered")


def list_all_user(username):
    for user in username:
        print(user)


if __name__ == '__main__':
    main()