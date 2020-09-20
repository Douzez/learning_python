"""
Given an integer, find the number of 1 bits it has.
23  ==> 10111   return  4 because there are 4 ones

Use the & (and) operator << not the AND >> 
    where 1 & 1 = 1, 0 & 1 = 0
Use the shift operator >> (right) and << (left)
"""

def one_bits(num):
    # fill this in
    count = 0
    while num > 0:
        print(num)
        if num & 1 == 1:
            count += 1
        num >>= 1 # ==> num = num >> 1
    return count

print(one_bits(23))
