# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isValidBST(self, root:TreeNode) -> bool:
		if root:
			res = validsubBST(root)
		else:
			res = True
		return res

def validsubBST(t):
	if not t:
		return True
	elif not (t.left or t.right):
		res = True
	elif isinstance(t.right, TreeNode):
		if isinstance(t.left, TreeNode):
			if t.left.val < t.val and t.right.val > t.val:
				res = validsubBST(t.right)
			else:
				res = False
		else:
			if t.right.val > t.val:
				res = validsubBST(t.right)
			else:
				res = False
	else:
		if isinstance(t.left, TreeNode):
			if t.left.val < t.val:
				res = validsubBST(t.right)
			else:
				res = False
		else:
			res = False
	return res