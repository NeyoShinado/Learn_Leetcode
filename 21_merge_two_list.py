'''
# Version1
# TC:O(N), SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		#init
		if l1 and l2:
			if l1.val > l2.val:
				res = ListNode(l2.val)
				l2 = l2.next
			else:
				res = ListNode(l1.val)
				l1 = l1.next
		elif l1:
			return l1
		elif l2:
			return l2
		else:
			return []

		index = res

		while l1 or l2:
			if l1 and l2:
				if l1.val > l2.val:
					index.next = ListNode(l2.val)
					l2 = l2.next
					index = index.next
				else:
					index.next = ListNode(l1.val)
					l1 = l1.next
					index = index.next
			elif l1:
				index.next = l1
				return res
			elif l2:
				index.next = l2
				return res

		# unnecessary
		return res
'''


# Version2
# 递归解决
class Solution:
	def mergeTwoLists(self, l1, l2):
		if not l1: return l2
		if not l2: return l1
		if l1.val <= l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2