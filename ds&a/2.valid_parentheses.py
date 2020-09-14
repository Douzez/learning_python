"""
Given a String contianing just the characters '[]{}()' determine if the input is valid.
Return True if valid, otherwise False
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets ust be closed in the correct order, with its corresponding open-clsoe bracket.
    3. A valid string is considered valid.


brackets = '[]{}()'  ===> True
brackets = '([]{})'  ===> True
brackets = '([]){'    ===> False
"""

def is_valid_brackets(brackets):
    if brackets == '':
        return True

    brackets_dictionary = { '(': ')', '[': ']', '{': '}' }

    stack = [] # LiFo

    for bracket in brackets:
        if bracket in brackets_dictionary:
            stack.append(bracket)
        elif brackets_dictionary[stack[-1]] == bracket:
                stack.pop()
    
    return True if len(stack) == 0 else False

brackets = '[]{}()'
print(is_valid_brackets(brackets))


brackets = '([]{})'
print(is_valid_brackets(brackets))

brackets = '([]{'
print(is_valid_brackets(brackets))
