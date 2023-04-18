ef main():
    print_menu()
    number = input()
    users = {}
    available_nums = {'1', '2', '3', '4', '5', '6'}
    while number not in available_nums:
        print("Please enter a number which corresponds to a function. ")
        print_menu()
        print("Please print one of the numbers")
        number = input()
    while number != '6':
        if number == '1':
            username_register(users)
            print_menu()
            number = input()
        if number == '5':
            list_all_user(users)
            print_menu()
            number = input()
        if number == '3' or number == '2':
            print("Please pick one of the options except 2, 3")
            print_menu()
            number = input()
        if number == '4':
            roles(users)
            print_menu()
            number == input()
    print("Thank you for using our secret chat!")
    quit()


def username_register(users):
    print("Please input your name below: ")
    name = input(': ')
    if name != "":
        if name in users:
            print('Username already exists please enter another one')
            name = input(': ')
            users["name"] = name
            users["role"] = 'user'
            print("Username " + name + " has been registered")
        elif name not in users:
            users["name"] = name
            users["role"] = 'user'
            print("Username " + name + " has been registered")
    elif name == "":
        print("Please enter something and do no leave blank.")
    return()


def roles(users):
    print("Type E if you want to exit assigning roles, else press any button to continue assigning roles.")
    choice = input(': ')
    while choice != 'E':
        roles_available = {'1', '2', '3'}
        print("Please print your username")
        role_name = input(': ')
        if role_name != users:
            print("1. User")
            print("2. Admin")
            print("3. Moderator")
            print("Which role to a sign?")
            role_picked = input(': ')
            if role_picked not in roles_available:
                print("Please write the number associated with the role.")
            else:
                if role_picked == '2':
                    if "admin" in users:
                        print("You are already registered as a admin, you cannot lower your role.")
                    elif "admin" not in users:
                        users["role: "] = "admin"
                        print("You are now registered as a admin.")
                if role_picked == '1':
                    print("You are already registered as a user.")
                if role_picked == '3':
                    if "moderator" in users:
                        print("You have already been registered as a moderator, you cannot lower your role.")
                    elif "moderator" not in users:
                        users["role: "] = "moderator"
                        print("You are registered as a moderator")
                choice = 'E'
        print("Please enter a username which exists already or the username you used when you registered.")
    main()



def list_all_user(users):
    for user in users:
        print(f"Name: {user}, Role: {users[user]}")
    return()


def print_menu():
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. Assign role")
    print("5. List all registered users")
    print("6. exit")


if __name__ == '__main__':
    main()
