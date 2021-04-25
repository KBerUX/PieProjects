# random game world

def start_here():
    str.lower(user_input=input(
        "Hi welcome to Random World!: do you want to play?: 'y' for Yes, 'n' for No: "))

    if user_input == 'y':
        print("I can't wait to begin with you!")
    elif user_input == 'n':
        user_input2 = input("Are you sure?: 'y' for Yes, 'n' for No:")
    else:
        user_input3 = input("Only Yes (y) or No (N) please :")


print(start_here())
