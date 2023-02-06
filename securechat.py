
print("1. Create user")
print("2. Login")
print("3. Connect to the chat")
print("4. List all registered users")
print("5. Exit")

number_answer = input()
while number_answer != '5':
    print("You have selected 'Create a user' press enter to go back.")
    back = input()
    if back == '':
        print("1. Create user")
        print("2. Login")
        print("3. Connect to the chat")
        print("4. List all registered users")
        print("5. Exit")
    elif number_answer == '2':
        print("You have selected 'Login' press enter to go back.")
        if back == '':
            print("1. Create user")
            print("2. Login")
            print("3. Connect to the chat")
            print("4. List all registered users")
            print("5. Exit")
    elif number_answer == '3':
        print("You have selected 'Connect to the chat' press enter to go back")
        if back == '':
            print("1. Create user")
            print("2. Login")
            print("3. Connect to the chat")
            print("4. List all registered users")
            print("5. Exit")
    elif number_answer == '4':
        print("You have selected 'List all registered users' press enter to go back")
        if back == '':
            print("1. Create user")
            print("2. Login")
            print("3. Connect to the chat")
            print("4. List all registered users")
            print("5. Exit")
    elif number_answer == '5':
        print("Thank you for using our secret chat!")
        quit()






