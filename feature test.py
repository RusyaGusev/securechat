

username = {}
print("Please enter your username.")
user = input(': ')
username["name"] = user
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

