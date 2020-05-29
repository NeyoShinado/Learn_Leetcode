# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		res = True
		node = head
		if not head or not(head.next):
			res = True
			return res
		# search tail
		while node:
			if node.next:
				node.next.pre = node
			else:
				tail = node
			node = node.next

		# case for N > 2
		while tail != head and tail != head.next:
			# odd and even situation
			if tail.val == head.val:
				tail = tail.pre
				head = head.next
			else:
				res = False
				return res

		#* special case for N = 2
		if tail.val != head.val:
			res = False

		return res