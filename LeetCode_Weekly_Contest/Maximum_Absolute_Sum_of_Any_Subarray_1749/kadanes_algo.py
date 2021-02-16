#!/bin/python

'''The program for the Kadane's algorithm explanation'''

def maxSubArray(n, arr):

    local_max = global_max = 0

    for i in range(n):
        local_max = max(arr[i], arr[i] + local_max)
        
        if local_max > global_max:
            global_max = local_max
    
    return global_max


if __name__ == '__main__':

    arr = [int(num) for num in input().split()]

    n = len(arr)

    result = maxSubArray(n, arr)

    print(result) 
