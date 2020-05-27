# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Version1 
# Brute Force
# 爆栈了
class Solution:
	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		if root:
			root.next = root.right
			tree_link(root, root.left)
		

def tree_link(parent, tree): 
	tree.next = tree.right
	if tree.left:
		tree.right = tree_link(tree, tree.left)
		del tree.left
	else:
		if tree.next:
			tree.right = tree_link(tree, tree.next)
			del tree.next
		else:
			if parent.next:
				parent.right = tree_link(parent, parent.next)
				del parent.next