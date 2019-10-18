import pizza

def cook_pizza():
    print('__name__ in cook_pizza function: ' + __name__)
    pizza.make_pizza()
    print('Turn oven on.')
    print('Place in oven.')
    print('Cook.')
    print('Remove and eat to your heart\'s desire.')

print('__name__ in bake.py: ' + __name__)
cook_pizza()
