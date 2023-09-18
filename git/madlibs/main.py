import random


'''def guess(x):
    random_num = random.randint(1, x)
    guess = 0

    while random_num != guess:
        guess = int(input(f"guess a number btw 1 and {x}: "))
        if guess > random_num:
            print(f"the guess is not close {x}")
        elif guess < random_num:
            print(f"the guess is close {x}")

    print(f"the guess is correct {random_num}")'''


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low, high)
        print(f'the guess should be between {low} and {high}')
        feedback = input(f"the guess {guess} too high (H), too low(L), correct (c): ").lower()

        if feedback == "h" and low != high:
            high = guess - 1
            print(f"the guess is too high: {guess}")
        elif feedback == "l":
            low = guess + 1
            print(f"the guess is too low {guess}")

    print(f"the guess is correct {guess}")


computer_guess(10)



'''def guess(x):
    random_num = random.randint(1, x)
    guess = 0

    while random_num != guess:
        guess = int(input(f"guess a number btw 1 and {x}: "))
        if guess > random_num:
            print(f"the guess is not close {x}")
        elif guess < random_num:
            print(f"the guess is close {x}")

    print(f"the guess is correct {random_num}")'''
