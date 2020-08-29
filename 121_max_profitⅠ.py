# Version0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	N = len(prices)
    	R = N-1
    	L = 0
    	map = {'in':prices[0], 'out':0, 'r_max':0, 'r_min':0, 'l_max':0, 'l_min':0}
    	profit = 0

    	if N < 2:
    		return profit

    	while R > L:
    		while prices[R-1] >= prices[R]:
    			map["out"] = R-1
    			R -= 1

    		while prices[L+1] <= prices[L]:
    			map["in"] = L+1
    			L += 1

    		map["r_min"]
    		if L == R-1:
    			profit = prices[R] - prices[L]
    			return profit
    		else:


# Version1
# 贪心思路
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init
        N = len(prices)
        res = 0
        if N == 0:
            return res
        
        dp = prices.copy()
        curMax = prices[-1]

        # traverse
        for i in range(N-1, 0, -1):
            if curMax > dp[i-1]:
                res = max(curMax-dp[i-1], res)

            else:
                curMax = dp[i-1]

        return res