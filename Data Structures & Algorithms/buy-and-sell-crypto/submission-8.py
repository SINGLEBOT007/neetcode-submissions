class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mpft = 0
        l,r = 0,1
        n = len(prices)

        
        mpft = 0
        l,r = 0,1
        n = len(prices)

        while r < n:
            if prices[l] < prices[r]:
                pft = prices[r] - prices[l]
                mpft = max(mpft, pft)
            else:
                l = r
            r+=1
        return mpft

    