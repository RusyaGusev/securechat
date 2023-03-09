#import random
name = "Jim"
question = "Will I win a lottery?"
#random_number = random.randint(1,9)
print("Please enter a number between 1 to 9")
selection = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
random_number = input(': ')
print(name + " asks: " + question)
print("Magic ball says: ")
while random_number not in selection:
    print("Please pick a number between 1, 9")
    break
else:
    if random_number == '1':
        print("Yes - definitely")
    elif random_number == '2':
        print("It is decidedly so")
    elif random_number == '3':
        print("Without a doubt")
    elif random_number == '4':
        print("Reply hazy, try again")
    elif random_number == '5':
        print("Ask again later")
    elif random_number == '6':
        print("Better not tell you now")
    elif random_number == '7':
        print("My sources say no")
    elif random_number == '8':
        print("Outlook not so good")
    elif random_number == '9':
        print("Very doubtful")



