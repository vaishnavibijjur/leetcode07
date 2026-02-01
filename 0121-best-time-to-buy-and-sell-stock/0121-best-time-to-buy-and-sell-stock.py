class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        res=0
        for p in prices:
            if p>low:
                res=max(res,p-low)
            else:
                low=p
        return res