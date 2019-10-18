#! /usr/bin/env python

def make_pizza():
    print('__name__ in make_pizza function: ' + __name__)
    print('Step 1: Create dough.')
    print('Step 2: Role dough.')
    print('Step 3: Add toppings.')
    print('Step 4: Add more cheese.')

if __name__ == '__main__':
    print('__name__ in conditional of pizza.py: ' + __name__)
    make_pizza()
