import random

number = random.randint(1, 100)
life = 5
print(number)
print('Welcome to the guessing number game')
print('1. Play the game')
print('2. Exit')

menu = input('Choose menu: ')

if menu == '1':
    while life > 0:
        guess = int(input('Enter your guess: '))
        if number == guess:
            print('Congratulations you\'re right')
            break
        else:
            print("Your guess is to big") if guess > number else print(
                "Your guess is to small")
            life -= 1
        print('Sorry your life points is empty, Thanks for playing')
        
