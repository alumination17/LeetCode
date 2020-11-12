# class Solution:
#     def minDeletions(self, s: str) -> int:

def minDeletions(s):

    d = {}

    for i in s: d[i] = d.get(i, 0) + 1  # if i exists in d, it will return its value, otherwise return 0 to avoid an error
                                        # overwrites 'no of occurences' (value) of corresponding letter (key) 
                                        # by No of times the 'key' appears in s
    seen = set()                        # set is used because needed to avoid duplicate frequencies
    deletions = 0
                            # while loop used because frequency will quit loop only when it will become unique for the set
    for f in d.values():    # iterate through each no of occurences (frequency) of each letter in dictionary
        while f in seen:    # if frequency already exists in set >> decrement duplicate frequency by 1 
             f -= 1
             deletions += 1 # increment 'deletions' by 1
        
        if f: seen.add(f) # checks if frequency still remains greater than 0 and adds frequency to 'seen' set

    return deletions
    



if __name__ == '__main__':

    s = input()

    result = minDeletions(s)

    print(result) 