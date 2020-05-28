# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		# init
		pos = 0
		res = False
		if head:
			if head.next:
				node = head

			else:
				res = False
				return res
		else:
			res = False
			return res


		while node.next:
			if not hasattr(node, "pos"):
				node.pos = pos
				pos += 1
				node = node.next
			else:
				res = True
				return True

		return res
