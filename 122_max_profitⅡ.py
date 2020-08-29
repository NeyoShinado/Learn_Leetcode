# Version 0
# 贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init
        res = 0
        N = len(prices)

        # traverse
        for i in range(1, N):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                res += diff
        return res