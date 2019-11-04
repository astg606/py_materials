x = 2

def func():
    '''
       This is a sample function
       contains in a module.
    '''
    print('Hi from within a module!')

if __name__ == '__main__':
    print("<> Running the module as a script! <>")
    print("The Value of x is: ", x)
    func()
