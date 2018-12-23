#this is a guess the number game.

import random


guessesTaken = 0

#ask user for name
print('hello! what is your name?')
myName = input()

#set range of numbers between 1 and 20
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

#loop through 6 numbers starting at 0
for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    #if statement
    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
