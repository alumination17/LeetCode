#!/bin/python3

''' You are given an integer array nums sorted in non-decreasing order.
Build and return an integer array result with the same length as nums such that result[i] is equal to the summation 
of absolute differences between nums[i] and all the other elements in the array.
In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).'''

class Solution:
    def getSumAbsoluteDifferences(self, nums) -> int:

# Here is naive brutal force approach which leads to TLE'''
        # for num in nums:
            
        #     temp_sum = 0
        #     j = 0
        #     while j < len(nums):
        #         temp_sum += abs(num - nums[j])
        #         j += 1
        #     result.append(temp_sum)
        # return result

#   as the array is sorted in non-decreasing order, each left number from nums[i] is less than or equal than nums[i], 
#   so does a right number. Therefore, we can write that: 
#   |num[i] - left_num| + |num[i] - num[i]| + |num[i] - right_num| ...
#   leads to the same pattern: 
#   (num[i] - left_num) + (num[i] - num[i]) + ... + (right_num - num[i]), etc
#   So we group this calculations and leave with:
#   [((i + 1) * num) - presum] + [(total_sum - presum) - (n - i - 1)*num] for each num in nums.'''

        result = []
        presum = 0 
        total_sum = sum(nums)
        n = len(nums)

        for i, num in enumerate(nums):
            presum += num
            temp_res = ((i + 1) * num - presum) + ((total_sum - presum) - (n - i - 1) * num)
            result.append(temp_res)
        
        return result
            
            
            
                