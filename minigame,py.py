def play():
    user = input("Let's play!: 'y' for yes and 'n' for no :)")
    if user == 'y':
        print("I can't wait to begin with you!")
    elif user == 'n':
        print("are you sure you don't want to continue?")
        user = input(
            "If that's the case, press 'y' if you still want to continue or 'n'")
        if user == 'y':
            print("sounds good!, let's begin!")
        else:
            print("Bye!")
    else:
        print("alright that's fine then")


print(play())
