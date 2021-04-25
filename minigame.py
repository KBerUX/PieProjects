# random game world


def start_here():
    user_input = input(
        "Hi welcome to Random World!: do you want to play?: 'y' for Yes, 'n' for No")
    if user_input == 'y' or 'Y':
        print("Let's begin then!")
    elif user_input == 'n' or 'N':
        print("Nevermind then!")
