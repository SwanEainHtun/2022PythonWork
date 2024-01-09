import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess number from 1 to {x}: "))
        #print(guess)
        if guess > random_number:
            print("It's much larger than my number!")
        elif guess < random_number:
            print("It's much less than my number! ")
    print(f"Congratulations! you have guessed my number-{random_number} correctly.")
guess(10)