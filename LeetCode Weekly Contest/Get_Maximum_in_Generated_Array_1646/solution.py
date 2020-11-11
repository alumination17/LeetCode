class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
                
        nums = [0]*n

        user_input = input()
        n = int(user_input[4])

        nums[0] = 0
        nums[1] = 1 
        
        for i in range(1,n):
            
            if (i * 2) >= 2 and (i * 2) <= n:
                nums[2 * i] = nums[i] 
            
            elif (i * 2 + 1) >= 2 and (i * 2 + 1) <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1] 

        return max(nums)