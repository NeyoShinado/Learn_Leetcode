class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		#init
		res = []
		l = '('
		r = ')'
		para = ['()']

		#* 生成字符串排列组合-递归