#!/bin/python3

'''You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        counter = 0
        
        for word in words:
            j = 0
            length = len(word)
            # for i in word:
            while j < length:
                
                if word[j] not in allowed:
                    break
                    
                j += 1
                
            if j == length:
                counter += 1
                    
        return counter