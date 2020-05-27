# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		subtree = []
		res = []

		if not root:
			# init
			res.append([root.val])
			if isinstance(root.left, TreeNode):
				subtree.append(root.left)
			if isinstance(root.right, TreeNode):
				subtree.append(root.right)
		else:
			return res

		#*
		while not subtree:
			new_subtree = []
			if isinstance(subtree[0], TreeNode):
				res.append([subtree[0].val])
				if isinstance(subtree[0].right, TreeNode):
					new_subtree.append(subtree[0].left)
				if isinstance(subtree[0].right, TreeNode):
					new_subtree.append(subtree[0].right)

			for t in subtree[1:]:
				res[-1].append([t.val])
				if isinstance(t.right, TreeNode):
					new_subtree.append(t.left)
				if isinstance(t.right, TreeNode):
					new_subtree.append(t.right)
			subtree = new_subtree

		return res