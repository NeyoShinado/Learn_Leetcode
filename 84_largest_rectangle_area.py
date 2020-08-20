# Version1
# 单调栈
# TC:O(N), SC:O(N)
# 无哨兵版本要做比较复杂的非空判断
class Solution:
    def largestRectangleArea(self, nums):
            N = len(nums)
        for i in range(N):
            # pop
            while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                left = stack.pop()
                while len(stack) > 0 and nums[i] == nums[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    weight = i - stack[-1] - 1
                else:
                    weight = i

                res = max(res, nums[left]*weight)
            # add
            stack.append(i)

        while len(stack) > 0 is not None:
            # 解决最小的柱形或者右端的递增柱形群
            curheight = nums[stack.pop()]
            while len(stack) > 0 and curheight == nums[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                weight = N - stack[-1] - 1
            else:
                weight = N
            res = max(res, curheight * weight)

        print(res)


# Version2
# 加哨兵版本
class Solution:
    def largestRectangleArea(self, nums):
        N = len(nums)
        res = 0
        nums = [0] + nums + [0]
        stack = [0]
        N += 2

        for i in range(1, N):
            while nums[i] < nums[stack[-1]]:
                left = nums[stack.pop()]
                width = i - stack[-1] - 1        
                #!注：最矮柱形弹出后，其左边界对应最左边的哨兵，所以宽度不会出错
                # 但要是采用先算宽度再弹出的策略这里就会出错
                res = max(res, left*width)
            stack.append(i)

        print(res)


# Version3
# 分治算法
# TC:O(NlogN), SC:O(N)
# 根据木桶原理将面积分为最小柱形部分，最小柱形左边和最小柱形右边三部分；迭代划分
# 但最佳解法还是单调栈，因为分治对有序柱形不起作用