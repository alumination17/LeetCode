
'''The program intends to apply Kadane's algorithm to Maximum Absolute Sum of Any Subarray problem.'''

import debugpy 
print("Starting debugger ...")
debugpy.listen(("localhost", 10001))
print("Waiting for clients to connect 🎉")
debugpy.wait_for_client()

def maxSubArray(n, arr):

    local_max = local_min = global_max = 0

    for i in range(n):
        # local_max = max(abs(arr[i]), abs(arr[i] + local_max))
        local_max = max(arr[i], arr[i] + local_max)
        local_min = min(arr[i], arr[i] + local_min)
        global_max = max(global_max, local_max, -local_min)
    
    return global_max


if __name__ == '__main__':

    print("Executing main function")
    
    arr = [int(num) for num in input().split()]

    n = len(arr)

    result = maxSubArray(n, arr)

    print(result) 
