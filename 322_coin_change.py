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


# Version 2
# 