
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
            username_register(username)
            print("1. Create a user")
            print("2. Login")
            print("3. Connect to the chat")
            print("4. List all registered users")
            print("5. exit")
            number = input()
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
    print("You have selected 'Register user' press enter to go back.")
    print("Please input your name below: ")
    name = input(': ')
    #print("Username " + name + " has been registered")
    if name in username:
        print('Username already exists please enter another one')
        name = input(': ')
        username.add(name)
    elif name not in username:
        username.add(name)
        print("Username " + name + " has been registered")
        return(username_register)

def list_all_user(username):
    print("You have selected 'list all users' press enter to go back.")
    for user in username:
        print(username)
    return(list_all_user)


if __name__ == '__main__':
    main()