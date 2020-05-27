# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not (isinstance(root.left, TreeNode) ^ isinstance(root.right, TreeNode)):
			if not root.left:
				res = True
			else:
				res = tree_equal(root.left, root.right)
		else:
			res = False
		return res

def tree_equal(lt, rt):
	res = True  #*

	if not (isinstance(lt, TreeNode) ^ isinstance(rt, TreeNode)):
		if not lt:
			res = True
		elif: lt.val == rt.val:
			if lt.left or lt.right or rt.left or rt.right:
				if tree_equal(lt.left, rt.right) and tree_equal(lt.right, rt.left):
					res = True
		else:
			res = False
	else:
		res = False

	return res