""" 
Keyword Arguments:
    Functions can be called using keyword arguments of the form ==> "kwarg=value"
"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()

# This function accepts one required argument (voltage) and three optional arguments
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments - voltage, state, action
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# dictionaries can deliver keyword arguments with the **-operator:
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)



""" 
When a final formal parameter of the form:
    - **name. it receives a dictionary, containing all keyword arguments 
        except for those corresponding to a formal parameter
    - *name. it receives a tuple, containing the postional arguments
        beyond the formal parameter list.
    - *name must occur before **name
"""

def cheese_shop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print('-- I am sorry, we are all out of', kind)
    print('*' * 40)
    
    for arg in arguments:
        print(arg)
    print('*' * 40)
    
    for keyword in keywords:
        print(keyword, ': ', keywords[keyword])

cheese_shop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")