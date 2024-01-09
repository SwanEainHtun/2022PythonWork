import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Choose Rock,Paper,Scissors : ").lower()
        if player == computer:
            print("computer : " + computer)
            print("player : " + player)
            print("Tie!")

        elif player == "rock":
            if computer == "paper":
                print("computer : " + computer)
                print("player : " + player)
                print("You lose!")
            elif computer == "scissors":
                print("computer : " + computer)
                print("player : " + player)
                print("You Win!")
        elif player == "paper":
            if computer == "rock":
                print("computer : " + computer)
                print("player : " + player)
                print("You Win!")
            elif computer == "scissors":
                print("computer : " + computer)
                print("player : " + player)
                print("You lose!")
        elif player == "scissors":
            if computer == "paper":
                print("computer : " + computer)
                print("player : " + player)
                print("You win!")
            elif computer == "rock":
                print("computer : " + computer)
                print("player : " + player)
                print("You lose!")
    play_again =input("Do you want to play again?(yes or no): ").lower()
    if play_again == "no":
        break
print("Bye!")


