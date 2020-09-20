"""
Optimized List sum

Crate a class that initializes with a list of numbers and has one method called sum.
sum() should take two parameters, start_idx and end_idx and return the sum of the list 
from start_idx (inclusive) to end_idx (exclusive).

[1,2,3,4,5,6,7] --> sum(2, 5) = 12 because 3 + 4 + 5

Use the precomputed sum, a rolling sum
in a new list, add the numbers in the list with the previous result in the new list
[1, 2, 3, 4,   5,  6,  7]
[1, 3, 6, 10, 15, 21, 28, 0]
"""

class ListFastSum:
    def __init__(self, nums):
        self.nums = nums
        self.sum_up_to = []

        current_sum = 0
        for num in nums:
            current_sum += num
            self.sum_up_to.append(current_sum)
        
        self.sum_up_to.append(0)
        print('Sum up to: ', self.sum_up_to)

    def sum(self, start_idx, end_idx):
        print('indexes - start: ', start_idx, ' - ', 'end: ', end_idx)
        end = self.sum_up_to[end_idx - 1]
        start = self.sum_up_to[start_idx - 1]
        print('indexes sum_up_to - start: ', start, ' - ', 'end: ', end)
        return end - start


nums = [1, 2, 3, 4, 5, 6, 7]
print(ListFastSum(nums).sum(2, 5))

nums = [11, 2, 32, 4, 50, 6, 70]
print(ListFastSum(nums).sum(5, 7))

