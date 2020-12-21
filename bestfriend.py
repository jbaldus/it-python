#!/usr/bin/python3

print('+-------------------+')
print('| Best Friend Maker |')
print('| By Mr. B          |')
print('+-------------------+')
print('')

while True:
    print("Hi, I'm the computer.")
    name = input("What's your name? ")
    color = input(f"Hi {name}! What's your favorite color? ")
    print(f"No way! My favorite color is also {color}!")
    movie = input("What's your favorite movie? ")
    print(f"What!?! My favorite movie is also {movie}!")
    game = input("What is your favorite game? ")
    print(f"Get out of here! My favorite game is {game}, too!")
    print(f"We like the same things! We should be best friends!")
    print('')
    response = input("Would you like to go again? (Y/n) ")
    if response.lower() in ["n", "no", "nope", "nu-uh"]:
        break