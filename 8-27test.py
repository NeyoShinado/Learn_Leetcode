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


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        if K != 2 and N % (K-1) != 1:
            return -1
        if N == 0:
            return 0


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # init
        s = 0    # 四个状态:0,90,180, 270
        N = len(grid)
        node = (0, 0)
        endNode = (N-1, N-2)
        cnt = 0
        queue = [[node, s]]
        nextQueue = []
        
        # BFS
        while queue:
            node, s = queue.pop(0)
            x, y = node
            cnt += 1

            if s == 0:
                # right
                if y+2 < N and grid[x][y+2] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # down
                if x+1 < N and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # spin right
                if x < N-1 and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 3])
                # spin left
                if x > 0 and grid[x-1][y] | grid[x-1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 1])

            elif s == 1:
                # right
                if y+1 < N and grid[x][y+1] | grid[x-1][y+1] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 1])
                # down
                if x+1 < N and grid[x+1][y] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # spin right
                if x < N-1 and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 3])
                # spin left
                if x > 0 and grid[x-1][y] | grid[x-1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 1])
                    if newNode == (N-1, N-1):
                        return cnt
            elif s == 2:
                # right
                if y+2 < N and grid[x][y+2] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # down
                if x+1 < N and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # spin right
                if x < N-1 and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 3])
                # spin left
                if x > 0 and grid[x-1][y] | grid[x-1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 1])
            else:
                # right
                if y+2 < N and grid[x][y+2] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # down
                if x+1 < N and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 0])
                    if newNode == endNode:
                        return cnt
                # spin right
                if x < N-1 and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 3])
                # spin left
                if x > 0 and grid[x-1][y] | grid[x-1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 1])
            

            if not queue:
                queue = nextQueue.copy()
                nextQueue = []
