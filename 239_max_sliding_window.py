# Version1
# Brute Force
# TC: O(NK), SC: O(N-K+1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if N * k == 0:
            return []
        return [max(nums[i:i+k]) for i in range(N-k+1)]


# Version2
# 双向队列
# TC: O(2N), SC: O(2N)
# 
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if N*k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # 删除不在滑动窗的元素
            if deq and deq[0] == i-k:   
                deq.pop(0)

            # 删除小于当前值的所有元素
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque
        deq = []
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, N):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output


# Version3
# 动态规划
# TC: O(3N), SC: O(3N)
# 该方法将数组依每K个元素划分成多个子组，最后一组若不满K个元素也划为一组
# 创建一个左向最大值数组left和右向最大值数组right
# 以左向为例，i索引上的值为其所在子组的左端到i元素的最大值
# 无论子窗口[i,j]与子组重合还是跨子组，该子窗的最大值即是max(right[i],left[j])
# 因为right[i]描述的是该子窗左端到组边界的最大值，left[j]描述的是该子窗右端到组边界的最大值
class Solution:
    def maxSlidingWindow(self, nums, k):
        N = len(nums)
        if N*k == 0:
            return []
        if k == 1:
            return nums

        # init
        left = [0] * N
        left[0] = nums[0]
        right = [0] * N
        right[N-1] = nums[N-1]

        for i in range(1, N):
            # update left_dir list
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])

            # update right_dir list
            j = N-i-1
            if (j+1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        output = []
        for i in range(N-k+1):
            output.append(max(left[i+k-1], right[i]))

        return output



# Others
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxnums=[]
        if k==1:
            maxnums=nums
        elif k==2:
            pre=nums[0]
            for num in nums[1:]:
                if num>pre:
                    maxnums.append(num)
                else:
                    maxnums.append(pre)
                pre=num
        else:
            maxv=max(nums[1:k])
            maxnums.append(max(nums[0],maxv))
            for i in range(k,len(nums)):
                if nums[i]>maxv:
                    maxv=nums[i]
                    maxnums.append(maxv)
                else:
                    maxnums.append(maxv)
                    if nums[i-k+1]==maxv:
                        maxv=max(nums[i-k+2:i+1])
        return maxnums
