##WHILE LOOP
#Inroduction
print('Welcome to guess the number!')
print('The rules are simple, I will think of a number, and you will try to guess it.')
#Import random generator
import random
#Allocate number range
number=random.randint(1,10)
#Only enter loop if guess is incorrect
isguessright = False
#Start of Loop
while isguessright !=True:
#User inputs guess
    guess = input('Guess a number between 1 and 10: ')
#If guessed number is correct then let user know they won and exit loop
    if int(guess) == number:
        print(f'You guessed {guess}. That is correct! you win!')
        isguessright = True
#If guesssed number  is incorrect then let user know and restart loop
    else:
        print(f"You guessed {guess}. Sorry that isn't it. Try again")

##FOR LOOP
print('Count to 10!')
for x in range (0,11):
    print(x)