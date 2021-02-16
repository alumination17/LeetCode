#!/bin/python3

'''You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] 
is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    - If x is a negative integer, then abs(x) = -x.
    - If x is a non-negative integer, then abs(x) = x.'''

def maxAbsoluteSum(nums): # here is modified Kadane's algorithm to be used
    # Key insight: The minimum and the maximum pointers are updated simultaneously because we need to return abs value
    
    local_max = local_min = global_max = 0
    n = len(nums)

    for i in range(n):
        local_max = max(nums[i], nums[i] + local_max) # local_max stores value of current max according to Kadane's algorithm
        local_min = min(nums[i], nums[i] + local_min) # local_min could take on the value of the most negative number
        global_max = max(global_max, local_max, -local_min)
    
    return global_max
   

if __name__ == '__main__':

    nums = [int(num) for num in input().split()]

    result = maxAbsoluteSum(nums)

    print(result) 