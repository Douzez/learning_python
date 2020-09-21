"""
Given an array of n positive integers and a postive integer s, find the minimal length of a contiguous subarray
which the sum is greater or equal than s.
If there isn't one return 0.

s = 7, nums = [2, 3, 1, 2, 4, 3]
r = 2, the subarray [4, 3] has the minimal length under the problem constrain.
"""
# USE TWO POINTERS

def min_subarray_sum_len(nums, s):
    res = float('inf')
    sum = 0
    left_pointer = 0
    right_pointer = 0

    while right_pointer < len(nums):
        sum += nums[right_pointer]
        while sum >= s:
            # Update the result
            res = min(res, (right_pointer - left_pointer + 1))
            # Update sum
            sum -= nums[left_pointer]
            # Increment left pointer
            left_pointer += 1
        # Increment right pointer
        right_pointer += 1
    if res == float('inf'):
        return 0
    else:
        return res

nums = [2, 3, 1, 2, 4, 3]
s = 7
print(min_subarray_sum_len(nums, s))

nums = [2, 3, 1, 2, 4, 3]
s = 9
print(min_subarray_sum_len(nums, s))