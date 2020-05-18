'''
#Version 1 
# 直接合并排序
class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		s = nums1 + nums2
		s.sort()
		N = len(s)
		if ((N % 2) == 1):
			res = s[int((N-1)/2)]
		else:
			res = (s[int(N/2)] + s[int(N/2 - 1)])/2
		return(res)
'''

'''
#Version 2 二分法
# 问题一般化为找到数组的第k个元素
# 如果有N个数组，就N分法，如此类推
class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		# specify short-long list
		if len(nums1) > len(nums2):
			l1 = nums2
			l2 = nums1
		else:
			l1 = nums1
			l2 = nums2
		del nums1, nums2
		
		# init
		N = len(l1) + len(l2)
		k = int(N / 2) + 1 # odd->k, even->k, k-1
		res = 0
		
		if N % 2 == 0:		## even list
			k = k - 1
			while(k > 1):
				n = int(k / 2)  # len of cmp_list
				if l1 and l2:		## l1 is not empty
					if len(l1) < n or len(l2) < n:	## shortest len < cmp_len
						n = min(len(l1), len(l2))

					if l1[n-1] <= l2[n-1]:	# remove n least elements
						l1 = l1[n:]
					else:
						l2 = l2[n:]
					k = k - n

				elif l2:
					res = (l2[k] + l2[k-1]) / 2
					return(res)

				else:
					res = (l1[k] + l1[k-1]) / 2
					return(res)

			for i in range(2):
				if l1 and l2:
					if l1[0] < l2[0]:
						res = res + l1[0]
						del l1[0]
					else:
						res = res + l2[0]
						del l2[0]

				elif l2:
					res = res + l2[0]
					del l2[0]

				else:
					res = res + l1[0]
					del l1[0]

			res = res / 2

		else:				# odd list
			while(k > 1):
				n = int(k / 2)  # len of cmp_list
				if l1 and l2:		## l1 is not empty
					if min(len(l1), len(l2)) < n:	## shortest len < cmp_len
						n = min(len(l1), len(l2))

					if l1[n-1] <= l2[n-1]:	# remove n least elements
						l1 = l1[n:]
					else:
						l2 = l2[n:]
					k = k - n

				elif l2:
					res = l2[k-1]
					return(res)

				else:
					res = l1[k-1]
					return(res)

			if l1 and l2:
				res = min(l1[0], l2[0])
			elif l2:
				res = l2[0]
			else:
				res = l1[0]

		return(res)
'''

#Version3
# 先用归并排序排出完整的数组，再根据奇偶取中位数
# 时间，空间复杂度都是O(m+n)

#Version4
# 类似归并排序对比两数组(m,n)，但通过指针代替合并数组，缩减SC
# 奇偶数组都需要遍历int(N/2)+1 次(偶数组需要多一个指针确定N/2 个数)
# 两指针astart,bstart 分别指定当前数组位置
# A组指针后移的判断句为astart<m && (bstart >= n||A[astart] < B[bstart])
# TC:O(m+n); SC:O(1)

#Version5
# 切分
# 奇数长：左半部分比右半部分大1(i+j=m-i+n-j+1)
# j=int((m+n+1) / 2 - i)，由于int(1/2)=0，奇偶数组ij取法都一样
# 且由0≤i≤m，0≤j≤n，需有m≤n
# 中位数的成立条件是A[i]≤B[j+1]&&B[j]≤A[i+1]
# 根据判断条件对i左右移，并考虑i={0,m}或j={0,n}的边界条件即可
# TC:应该为O(min(m,n));SC:O(1)
