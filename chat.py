
def main():
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. List all registered users")
    print("5. exit")
    number = input()
    usernames = set
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
            username_register(usernames)
        elif number == '4':
            list_all_user(usernames)
            print("1. Create a user")
            print("2. Login")
            print("3. Connect to the chat")
            print("4. List all registered users")
            print("5. exit")
            number = input()
    print("Thank you for using our secret chat!")
    quit()


def username_register(usernames):
    print("Please input your name below: ")
    name = input(': ')
    while name in usernames:
        print('Username already exists please enter another one')
        name = input(': ')
    usernames.add(name)
    print("Username " + name + " has been registered")


def list_all_user(usernames):
    for user in usernames:
        print(user)
    return list_all_user()

if __name__ == '__main__':
    main()