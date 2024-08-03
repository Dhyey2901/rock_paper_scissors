import random

while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock , paper, scissors ?")

    print("computer: ", computer)
    print("player: ", player)

    if player == 'rock':

        if computer == 'paper':
            print("player wins")

        elif computer == 'scissors':
            print("player wins")

        else:
            print("play once again")

    elif player == 'paper':

        if computer == 'paper':
            print("play once again")

        elif computer == 'scissors':
            print("Computer wins")

        else:
            print("player wins")
    else:

        if computer == 'paper':
            print("player wins")

        elif computer == 'rock':
            print("Computer wins")

        else:
            print("play once again")

    play_again = input("Wanna play again? (yes/no)? ").lower()

    if play_again != 'yes':
        break

print("Bye!Bye")