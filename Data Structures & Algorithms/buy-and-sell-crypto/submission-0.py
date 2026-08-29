class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        cmin, cmax = float('inf'), 0
        for i in prices:
            cmin = min(cmin, i)
            mp = max(i - cmin, mp)
        return mp
        