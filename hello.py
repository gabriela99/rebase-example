#!/usr/bin/env python3
from datetime import datetime

def say_time():
    print('it is', datetime.now())

def ask_for_name():
    name = input('please enter your name: ')
    print('hi', name)
    print('have a nice day!')

if __name__ == '__main__':
<<<<<<< HEAD
    ask_for_name()
=======
    greeting()
    say_time()
>>>>>>> say the current time
