"""A number-guessing game."""
from random import randint

number = randint(1,100)
count = 0

#greet player 
print('hi')

#get player name 
print('What is your name?')
print('Enter your name')

name = input('(type in your name)')

print(f"Hello, {name}, I'm thinking of a number between 1 and 100.")
print('Try to guess my number.')



while True: 
    guess = input('Your guess?')

    #make sure the guess is actually a number 
    try: 
        guess = int(guess)
    except ValueError:
        print(f'{guess} is not a valid number, try again')
        continue

    if guess > number: 
        print('Your guess is too high, try again.')
        count += 1 
    if guess < number: 
        print('Your guess is too low, try again.')
        count += 1
    if guess == number: 
        count += 1
        print(f'Well done, {name}! You found my number in {count} tries!')
        break