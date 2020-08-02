'''
# Version0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		# init
		res = None
		height = 1
		node = root

		if p == root or q == root:
			res = root
			return res
		elif p == q:
			res = p
			return q

		# pq scan
		node = scan(node, height, p, q)

		# backtrack
		if p.height  == q.height:
			if p.parent == q.parent:
				res = p.parent
				return res
			else:
				node = p.parent

		elif p.height > q.height:
			node = p.parent
		else:
			node = q.parent

		while node != root:
			if node == q:
				res = q
				return res
			if node == p:
				res = p
				return res
			else:
				node.check = True
			node = node.parent
		
		# search commmon ancestor
		if p.height < q.height:
			node = p.parent
		else:
			node = q.parent
		while node!= root:
			if hasattr(node, 'check'):
				res = node
				return res
			else:
				node = node.parent
		res = root

		return res


def scan(node, height, p, q):
	node.height = height
	height += 1
	if node == p or node == q:
		return node
	else:
		if node.left:
			node.left.parent = node
			node.left = scan(node.left, height, p, q)
		if node.right:
			node.right.parent = node
			node.right = scan(node.right, height, p, q)
'''


# Version1
# 递归
# TC: O(N), SC: O(N)
# fx表示x的子树包含p或q；flson指左子树包含p或q，frson表示右子树包含p或q；
# 公共祖先的判别式为(flson && frson)||((x==p || x==q)&&(flson||frson))
# 由于DFS是自底向上递归，公共祖先的两种情况(是其中一个节点；不是其中的节点，节点一定分布于左右子树)
# 就已经交代清楚了，找到的公共祖先一定是深度最大的(最近)

class Solution:
	res = None

	def dfs(self, root, p, q):
		if root == None:
			return False

		lson = self.dfs(root.left, p, q)
		rson = self.dfs(root.right, p, q)

		if (lson and rson) or ((root==p or root==q) and (lson or rson)):
			self.res = root

		return lson or rson or (root==p or root==q)

	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
		self.dfs(root, p, q)
		return self.res


# Version2
# 存储父节点
# TC: O(N), SC: O(N)
# Not pass
# ⭐Dict KeyError
class Solution:

	parent = dict()
	visited = set()

	def dfs(self, root):
		if not root.left:
			parent[root.left.val] = root
			self.dfs(root.left)
		if not root.right:
			parent[root.right.val] = root
			self.dfs(root.right)


	def lowestCommonAncestor(self, root, p, q):
		self.dfs(root)
		while p:
			self.visited.add(p.val)
			p = self.parent.get(p.val)
		while q:
			if q.val in self.visited:
				return q
			q = self.parent.get(q.val)

		return 





