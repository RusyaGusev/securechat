def main():
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
            number = input()
    print("Thank you for using our secret chat!")
    quit()


def username_register(users):
    userinfo = {}
    print("Please input your name below: ")
    username = input(': ')
    if username != "":
        if username in users:
            print('Username already exists please enter another one')
            name = input(': ')
            print("Username " + name + " has been registered")
        elif username not in users:
            print("Username " + username + " has been registered")
        userinfo["username"] = username
        userinfo["Role"] = 'user'
        users[username] = userinfo
    elif username == "":
        print("Please enter something and do no leave blank.")
    return()


def roles(users):
    new_role = {}
    print("Type E if you want to exit assigning roles, else press enter to assign role.")
    choice = input()
    while choice != 'E':
        roles_available = {'1', '2', '3'}
        print("Please print your username")
        role_name = input(': ')
        if role_name in users:
            print("1. User")
            print("2. Admin")
            print("3. Moderator")
            print("Which role to a sign?")
            role_picked = input(': ')
            if role_picked not in roles_available:
                print("Please write the number associated with the role.")
            else:
                if role_picked == '2':
                    if 'admin' not in users[role_name]:
                        new_role["Role: "] = 'admin'
                        print("You are now registered as a admin.")
                    if 'admin' in users[role_name]:
                        print("You are already registered as a admin.")
                    if 'moderator' in users[role_name]:
                        print("You are registered as a moderator and hence you cannot lower your role.")
                if role_picked == '1':
                    if 'admin' or 'moderator' not in users[role_name]:
                        print("You are already registered as a user.")
                    elif 'moderator' or 'admin' in users[role_name]:
                        print("You are registered as a moderator or admin hence you cannot lower your role.")
                if role_picked == '3':
                    if 'moderator' not in users[role_name]:
                        new_role["Role: "] = 'moderator'
                        print("You are already registered as a moderator.")
                    if 'moderator' in users[role_name]:
                        print("You are already registered as a moderator")
                choice = 'E'
                users[role_name] = new_role
        print("Please enter a username with which you registered.")
    return()


def list_all_user(users):
    for user in users:
        print(f"User: {user}, {users[user]}")
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
