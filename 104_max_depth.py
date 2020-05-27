# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if root:
			res = Depthtree(root)
		else:
			res = 0
		return res

def Depthtree(tree):
	if tree.left and tree.right:
		res = max(Depthtree(tree.left), Depthtree(tree.right)) + 1
	elif tree.left:
		res = Depthtree(tree.left) + 1
	elif tree.right:
		res = Depthtree(tree.right) + 1
	else:
		res = 1
	return res