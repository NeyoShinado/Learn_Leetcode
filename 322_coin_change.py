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
# Not pass(爆栈)
# 递归树，按面值划分，自上而下
# F(S)为组成金额S所需的硬币数量，[c0,...,cn-1]为可选的面值
#!最优子结构F(S) = F(S-C) + 1
# 子问题变成枚举c0-cn-1并选F(S)的最小值
# F(S)=minF(S-ci)+1, s.t.S-ci≥0
# 用字典记录S子状态的最小数目，避免重复计算
# TC: O(Sn), SC: O(S)，S为状态的数目
class Solution:
	def coinChange(self, coins, amount):
		# 从大面值开始筛选，减少重复计算次数
		coins.sort(reverse=True)
		if amount < 1:  # 默认面值≥1
			return 0
		return change(coins, amount, {amount:1e9})

#!count记录数额的最小数目缓存
def change(coins, res, count):
	if res < 0:
		return -1
	if res == 0:
		return 0
	#!计算过当前面值，直接返回，避免重复计算
	if count.get(res,1e9) != 1e9:
		return count[res]

    # 枚举面值，算出当前面额的最小硬币数
	curmin = 1e9
	for coin in coins:
		res = change(coins, res-coin, count)
		if res > 0 and res < curmin:
			curmin = res + 1
	count[res] = -1 if curmin == inf else curmin
	return count[res]
'''


# Version 3
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
