# 18'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		res = None
		node = None

		# special case
		if not head:
			return res
		elif not head.next:
			res = head
			return res

		while head:
			if head.next:
				node = head.next
				node.pre = head
				if hasattr(head, 'pre'):
					head.next = head.pre
					del head.pre
				else:
					head.next = None
				head = node
			else:
				head.next = head.pre
				del head.pre
				res = head
				return res
