
def main():
    print_menu()
    number = input()
    username = {}
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
            print("Username " + name + " has been registered")
        elif name not in username:
            username.add(name)

            print("Username " + name + " has been registered")
            username_set = len(username)
    return(username_register)

user_role2 = {}
roles_available = {'1', '2', '3'}
def roles(username, user_role2):
    print("Please print your username")
    role_name = input(': ')
    user_role2["name"] = role_name
    if user_role2 == username:
        print("1. User")
        print("2. Admin")
        print("3. Moderator")
        print("Which role to a sign?")
        role_picked = input(': ')
        if role_picked not in roles_available:
            print("Please write the number associated with the role.")
        else:
            if role_picked == '2':
                user_role2["name"] = role_name
                user_role2["role"] = "admin"
                print("You are now registered as a admin.")
                if "admin" or "moderator" in user_role2:
                    print("You are either already registered as a admin or you are registered "
                          "as a moderator in which case you cannot lower your position")
            if role_picked == '1':
                print("You are already registered as a user.")
            if role_picked == '3':
                user_role2["name"] = role_name
                user_role2["role"] = "moderator"
                print("You are registered as a moderator")
                if "moderator" in user_role2:
                    print("You are already registered as a moderator.")
    else:
        print("Please enter a username which exists already or the username you used when you registered.")
roles(username, user_role2)
def list_all_user(username):
    print("You have selected 'list all users' press enter to go back.")
    for user in username:
        print(username)
    return(list_all_user)







def print_menu():
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. Assign role")
    print("5. List all registered users")
    print("6. exit")


if __name__ == '__main__':
    main()
