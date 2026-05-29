class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mxl = 0
        l = 0
        n = len(s)
        sset = set()

        for r in range(n):

            while s[r] in sset:
                sset.remove(s[l])
                l+=1
            
            win = (r-l)+1
            mxl = max(mxl, win)
            sset.add(s[r])
        
        return mxl