# 20'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		# init
		res = None

		# special case
		#* 注意优先级
		if not (headA or headB):
			return res
		
		node = headA
		while node:
			node.check = True
			if hasattr(node, 'next'):
				node = node.next
			else:
				break

		node = headB
		while node:
			if hasattr(node, 'check'):
				res = node
				return res
			if hasattr(node, 'next'):
				node = node.next
			else:
				node = None

		return res