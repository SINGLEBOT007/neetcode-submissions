class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mpft = 0
        l,r = 0,1
        n = len(prices)

        while r<n:
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                pft = prices[r] - prices[l]
                mpft = max(mpft, pft)
                r+=1
        return mpft