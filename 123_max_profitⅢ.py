# Version0
# No pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init
        N = len(prices)
        res = 0
        # 各阶段的最大利润，分别为2持有第一股，3售出第一股，4持有第二股，5售出第二股
        dp = [[0, 0, 0, 0] for _ in range(N)]
        dp[0][0] = -prices[0]

        # dp
        for i in range(1, N):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i]+dp[i-1][0])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
            dp[i][3] = max(dp[i-1][3], prices[i]+dp[i-1][2])
            res = max(res, dp[i][1], dp[i][3])
        return res

# Version1
# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init
        N = len(prices)
        if N < 1:
            return 0
        # dp[i][k][0/1] 第i天至多买卖k次且持股与否时的最高利润
        '''
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(N)]
        dp[1][1][0] = 0
        dp[1][1][1] = -prices[1]
        dp[1][2][0] = 0
        dp[1][2][1] = -prices[1]        #* 最少k次交易为的是直接维护最优解

        # dp
        for i in range(2, N):
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1]+prices[i])
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0]-prices[i])
        '''
        # 空间优化
        # init
        pOne0 = 0
        pOne1 = -prices[0]
        pTwo0 = 0
        pTwo1 = -prices[0]
        for i in range(1, N):
            pTwo0 = max(pTwo0, pTwo1+prices[i])
            pTwo1 = max(pTwo1, pOne0-prices[i])
            pOne0 = max(pOne0, pOne1+prices[i])
            pOne1 = max(pOne1, -prices[i])

        return pTwo0