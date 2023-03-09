
def main():
    print_menu()
    roles = set()
    number = input()
    username = set()
    available_nums = {'1', '2', '3', '4', '5', '6'}
    while number not in available_nums:
        print("Please enter a number which corresponds to a function. ")
        print_menu()
        print("Please print one of the numbers")
        number = input()
    while number != '6':
        if number == '1':
            username_register(username)
            print_menu()
            number = input()
        elif number == '5':
            list_all_user(username)
            print_menu()
            number = input()
        if number == '3' or number == '2':
            print("Please pick one of the options except 2, 3")
            print_menu()
            number = input()
        if number == '4':
            roles()

    print("Thank you for using our secret chat!")
    quit()


def username_register(username):
    print("You have selected 'Register user' press enter to go back.")
    print("Please input your name below: ")
    name = input(': ')
    if name == "":
        print("Please enter something and do no leave blank.")
        if name in username:
            print('Username already exists please enter another one')
            name = input(': ')
            username.add(name)
            user.add(name)
            print("Username " + name + " has been registered")
        elif name not in username:
            username.add(name)
            user.add(name)
            print("Username " + name + " has been registered")
            username_set = len(username)
    return(username_register)

def list_all_user(username):
    print("You have selected 'list all users' press enter to go back.")
    for user in username:
        print(username)
    return(list_all_user)

user = set()
admin = set()
moderator = set()
def roles(username):
    print("Print the username:")
    role_name = input(':')
    while role_name in username == True:
        print("1. User")
        print("2. Moderator")
        print("3. Admin")
        print("Which role to asign?")
        role_picked = input(': ')
        if role_picked == 'admin':
            admin.add(username)
            print("You are now registered as a admin.")
        if role_picked == 'user':
            print("You are already registered as a user.")
        if role_picked == 'moderator':
            moderator.add(username)
            print("You are registered as a moderator")
        elif username in moderator:
            print("User already registered as moderator")

def print_menu():
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. Assign role")
    print("5. List all registered users")
    print("6. exit")


if __name__ == '__main__':
    main()
