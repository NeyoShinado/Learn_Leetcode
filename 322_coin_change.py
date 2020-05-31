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