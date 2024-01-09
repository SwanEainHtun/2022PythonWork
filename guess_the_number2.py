import random
def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        guess = random.randint(low,high)
        feedback = input(f"Is my number {guess } too lower(L) or too high(H) ").upper()
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print("I guessed your number correctly.")
guess(10)