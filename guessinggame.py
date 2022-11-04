#Guess within 5 tries what number the computer is thinking between 1 and 20

import random
number = random.randint(1, 20)

print("Hi! What's your name?")
player_name = input()
number_of_guesses = 0
print('Welcome ' + player_name+ '!  Can you guess what number I am thinking of between 1 and 20:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
         print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number)) 
