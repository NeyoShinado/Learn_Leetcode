'''
# Version 0
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		# init
		id = 0
		res = 0
		N = len(coins)
		coins.sort(reverse = True)

		if amount == 0:
			return res

		while amount != 0 and id <= N-1:
			if amount >= coins[id]:
				res = res + amount // conis[id]
				amount = amount % coins[id]
			else:
				id += 1

		if amount != 0:
			res = -1
		return res
'''


'''
# Version 1
# 搜索回溯
# 超时
# 根据各面值的取法(数量)进行回溯遍历
# 设有n种面值，总金额S，求minΣxi,s.t.Σxi*ci=S
# TC: O(S^n), SC: O(n)
class Solution:
	def coinChange(self, coins, amount) -> int:
		return change(0, coins, amount)

def change(idxCoin, coins, amount):
	if amount == 0:
		# 匹配完成，无需额外硬币
		return 0
	if idxCoin < len(coins) and amount > 0:
		maxval = amount // coins[idxCoin]
		minCost = inf
		for id in range(0, maxval+1):
			if amount >= id * coins[idxCoin]:
				#*总额递归前进行划分，免去回溯步骤
				res = change(idxCoin + 1, coins, amount - id*coins[idxCoin])
				if res != -1:
					#*硬币个数回溯计数
					minCost = min(minCost, res + id)
		return -1 if minCost == inf else minCost
	return -1
'''


'''
# Version 2
# TC: O(SN), SC: O(S)
#*S为金额，N为面值数，当S较大时正常递归树将爆栈，所以要使用缓存机制
#*python lru_cache记忆功能跳过重复子函数，加速递归
import functools

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		@functools.lru_cache(amount)
		def dp(rem):
			if rem < 0: return -1
			if rem == 0: return 0
			mini = int(1e9)
			for coin in self.coins:
				res = dp(rem - coin)
				if res >= 0 and res < mini:
					mini = res + 1
			return mini if mini < int(1e9) else -1

		self.coins = coins
		if amount < 1: return 0
		return dp(amount)
'''


# Version 3
# 动态规划，自下而上
# F[S] = min(F[S-ci])+1, S-ci≥0
# TC: O(SN), SC: O(N)
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		# init
		res = 0
		dp = [float("inf")] * (amount+1)
		dp[0] = 0

		'''慢些，类似于Floyd的更新方式
		for coin in coins:
			for x in range(coin, amount + 1):
				dp[x] = min(dp[x], dp[x - coin] + 1)
		'''
		for i in range(1, amount+1):
			#*小于面值的金额不能凑成
			if i < min(coins):
				continue
			dp[i] = min([dp[i-coin] for coin in coins if i-coin >= 0]) + 1

		return dp[amount] if dp[amount] != float('inf') else -1
