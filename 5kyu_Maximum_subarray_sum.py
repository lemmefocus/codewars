"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""

def max_sequence(arr: list):
    compare, loop = 0, arr.copy()
    if len(arr) > 0:
        for i in range(len(loop)):
            copied_arr = arr.copy()
            for j in range(len(arr)):
                my_sum = sum(copied_arr)
                if my_sum > compare:
                    compare = my_sum

                copied_arr.pop()
            arr.pop(0)

        return compare
    else:
        return 0
