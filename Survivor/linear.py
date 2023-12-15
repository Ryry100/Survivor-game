'''linear equation in the form of ax + b = c checks answer person solves equation'''

import random
def linear():
    #get three random numbers
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)


    while a == 0:
        a = random.randint(-100, 100)

    #create equation and let person solve
    print('Solve the following equation \n')
    print(f'{a}x + {b} = {c}')

    x = (c - b) / a
    print(x)
    user_answer = float(input('Enter your solution(if forever decimal, then enter 14 decimal digits):  '))
    if user_answer == x:
        print('Correct')
    else:
        print(f'Sorry, the correct answer is {x}')
        do_again = input('Do you want to try again?   ')
        if do_again == 'yes':
            linear()
        elif do_again == 'no':
            quit()
        else:
            do_again = input('Do you want to try again?   ')
linear()