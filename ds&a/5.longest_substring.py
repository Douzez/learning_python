""" NO LE ENTIENDO!!!!!!  :(

Given a String, find the length of the longest substring without repeating characters.

str = 'pwwkew'
output = 3  --> 'wke' is the longest substring without repeating chars.
"""

def length_longest_substring(str='pwwkew'):
    letters = {}
    tail = -1
    head = 0 # index of current letter
    result = 0

    while head < len(str):
        if str[head] in letters:
            tail = max(tail, letters[str[head]])
        letters[str[head]] = head
        result = max(result, head - tail)
        head += 1
        print()
        print(str)
        print('letters: ', letters)
        print('tail ', tail)
        print('head ', head)
        print('result ', result)
    return result

length_longest_substring()
