import random as r

number = r.randint(1, 100)

while True:
    guess = int(input('\nВведите цифру: '))
    
    if guess < number:
        print('Ваше число меньше того, что загадано')
        
    if guess > number:
        print('Ваше число больше того, что загадано')
        
    if guess == number:
        print('Отличная интуиция! Вы угадали число :)')
        break
