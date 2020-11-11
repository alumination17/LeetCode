# class Solution:
def getMaximumGenerated(n):
        
    nums = [0,1]

    if n < 2:
        return max(nums[:n+1])
        
    for i in range(2,n+1):

        if i % 2 == 0:
            nums.append(nums[i//2])

        else:
            nums.append(nums[i//2] + nums[(i+1)//2])

    return max(nums)

if __name__ == '__main__':

    n = int(input())

    result = getMaximumGenerated(n)

    print(result)
