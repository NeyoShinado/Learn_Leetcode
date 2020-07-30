# Version1
# TC: O(N), SC: O(1)
# 买入卖出两种操作可以整合为同一个收益，即买入为正收益，卖出为负收益
# 设i天后的最大收益，可划分为三种状态：
# ①第i天持有一支股票；②不持有股票且处于冷冻期；不持有股票且不处于冷冻期
# f[i]完全由f[i-1]确定，所以只要三个变量就足够了
# 第N日的最大利益=max(f[N-1][1], f[N-1][2])
class Solution:
	def maxProfit(Self, prices: List[int]) -> int:
		if not prices:
			return 0

		N = len(prices)
		f0, f1, f2 = -prices[0], 0, 0
		for i in range(1, N):
			newf0 = max(f0, f2 - prices[i])
			newf1 = f0 + prices[i]
			newf2 = max(f1, f2)
			f0, f1, f2 = newf0, newf1, newf2

		return max(f1, f2)