#!/usr/bin/python3

print('+-----------------+')
print('| GUESS MY NUMBER |')
print('| By Mr. B        |')
print('+-----------------+')
print('')

name = input('What is your name? ')

print('')
num = 42
print("I'm thinking of a number between 0 and 100. Can you guess it?")
guess = -1
while guess != num:
    guess = input("What is your guess? ")
    guess = float(guess)
    if guess < num:
        print("Sorry, too low. Guess again.")
    elif guess > num:
        print("Sorry, too high. Guess again.")
    

print(f"Congratulations, {name}! You win!")