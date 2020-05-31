# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
    	res = 0
    	node = root

    	while node != True:
    		node = all_check(root)
		    candid = sum (node all two step) and set node.check
	    	res = max(res, candid)
	    return res


#* add pre
def all_check(node):
	res = True
	if node:
		if hasattr(node, 'check'):
			if node.left:
				res = all_check(node.left)
			if res == True and node.right:
				res = all_check(node.right)
			elif res != True and node.right:
				continue
		else:
			res = node
	else:
		return True


#*
def two_step_sum(node):
	res = 0
	res = node.val + two_step_sum(node.left.left) + two_step_sum(node.left.right) + two_step_sum(node.right.left) + two_step_sum(node.right.right) + two_step_sum(node.pre.leftorright)
	return res