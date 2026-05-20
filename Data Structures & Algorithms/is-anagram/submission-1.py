from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)

        #optimal approach using hashmap
        # if len(s) != len(t):
        #     return False
        
        # hash={}

        # for char in s:
        #     hash[char] = hash.get(char, 0)+1
        # for char in t:
        #     hash[char] = hash.get(char, 0)-1

        # for value in hash.values():
        #     if value != 0:
        #         return False
        
        # return True

        # optimal approach using defaultdict

        if len(s)!=len(t):
            return False
        
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1

        for value in count.values():
            if value!=0:
                return False

        return True

        