from random import randint
import sys
sys.argv
a=int(sys.argv[1])
b=int(sys.argv[2])
answer = randint(a,b)
while True:
    try:
        guess = int(input('Enter your guess  '))
        if a<=guess<=b:
            if guess==answer:
                print('Right Answer')
                break
        else:
            print(f'Hey! We want a number between {a} and {b}')
    except ValueError:
        print('Please enter a number')
        continue
print ('Thanks for playing')


