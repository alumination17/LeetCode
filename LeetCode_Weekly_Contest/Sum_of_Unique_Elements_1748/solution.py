#!/bin/python3
'''You are given an integer array nums. The unique elements of an array are the elements that appear 
exactly once in the array. Return the sum of all the unique elements of nums.

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

# class Solution:
    # def sumOfUnique(self, nums: list[int]) -> int:
def sumOfUnique(nums):
   
    d = {}
    summ = 0
        
    for i in nums: 
        d[i] = d.get(i, 0) + 1 # if i exists in d, it will return its value, otherwise return 0 to avoid an error
                                # overwrites 'no of occurences' (value) of corresponding letter (key) 
                                # by No of times the 'key' appears in nums
    for i, j in d.items():      # check if value in d (No of appearances) equals to 1 which means 
        if j == 1:              # that those elements (stored in keys) are unique
            summ += i           # and add them to summ
    
    return summ

if __name__ == '__main__':

    nums = [int(num) for num in input().split()]

    result = sumOfUnique(nums)

    print(result) 