
def game():
    import random

    game_list = ["R", "P", "S"]
    cpu = random.choice(game_list)
    player = input("Please select an option between R, P or S: ")

    while True:
        print(f"Player({player}) : CPU({cpu})")
        if player == cpu:
            print("It's a tie")
            break
        elif player == "P":
            if cpu == "R":
                print("You won")
            else:
                print("You lost")
                break
        elif player == "R":
            if cpu == "S":
                print("You won")
            else:
                print("You lost")
                break
        elif player == "S":
            if cpu == "P":
                print("You won")
            else:
                print("You lost")
                break
        else:
            print("You have selected an invalid option, please try again")
        break


game()
