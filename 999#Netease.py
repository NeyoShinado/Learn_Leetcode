# 小易放积木
#! usr/etc/bin python
#coding: utf-8
'''
思路：跟小易遍历一遍，使用贪心思维，尽可能以边界状态满足条件
①堆的数量尽可能小
②各堆相差一
③包里尽可能多
一旦不满足，报错
'''

class Solution:
    def ascendHeap(self):
        # input
        T = int(input())
        # main loop
        for i in range(T):
            N, m = list(map(int, input().split(" ")))
            H = list(map(int, input().split(" ")))

            # start walking
            for loc in range(N):
                if loc == 0:
                    m += H[0]
                    H[loc] = loc
                else:
                    gap = H[loc] - H[loc-1] - 1
                    if gap == 0:
                        continue
                    elif gap > 0:    # larger
                        m += gap
                        H[loc] -= gap
                    else:   # smaller, need bag
                        gap *= -1
                        if m >= gap:
                            m -= gap
                            H[loc] += gap
                        else:
                            print("NO")
                            break
            if loc == N-1:
                print("YES")


if __name__ == "__main__":
    t = Solution()
    t.ascendHeap()


#*跳桩
# Version1
# DFS
# 超时
import sys
sys.setrecursionlimit(100000000)

class Solution:
    def jumpStand(self):

        def DFS(index, buff):

            if index == N-1:
                return True

            for i in range(index+1, min(index+k+1, N)):
                if H[index] >= H[i]:
                    if DFS(i, buff):  # normal
                        return True   # 提前剪枝
                if buff and H[index] < H[i]:
                    if DFS(i, 0):  #* 用buff的时机是否有讲究
                        return True
            return False

        # input
        T = int(input())
        for t in range(T):
            N, k = list(map(int, input().split(" ")))
            H = list(map(int, input().split(" ")))

            res = DFS(0, 1)
            if res:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    t = Solution()
    t.jumpStand()


# Version2
# DP
# Not pass
# #! usr/etc/bin python
#coding: utf-8
# DFS
class Solution:
    def jumpStand(self):

        # input
        T = int(input())
        # main loop
        for t in range(T):
            N, k = list(map(int, input().split(" ")))
            H = list(map(int, input().split(" ")))

            # init
            dp = [[False] * N for _ in range(2)]  # 行表示buff状态，值表示能否到达
            dp[0][0], dp[1][0] = True, True
            end = 1

            # DP
            while end < N:
                index = end - 1
                while not dp[1][end] and index >= max(0, end-k):
                    if H[end] <= H[index]:
                        dp[1][end] |= dp[1][index]
                    index -= 1
                failCnt = end - index - 1

                index = end - 1
                while not dp[0][end] and index >= max(0, end-k):
                    if H[end] <= H[index]:
                        dp[0][end] |= dp[0][index]
                    else:
                        dp[0][end] |= dp[1][index]
                    index -= 1
                failCnt = max(end - index - 1, failCnt)

                # 如果不能跳的长度==K，后面的也不可能达到，返回False
                if failCnt >= k:
                    break

                end += 1

            if dp[0][-1] or dp[1][-1]:
                print("YES")
            else:
                print("NO")



if __name__ == "__main__":
    t = Solution()
    t.jumpStand()


# Version3
# 多状态DP
# 0表示不能到达，1表示有buff到达，2表示无buff到达
# 同样Not Pass
class Solution:

    def main(self):

        def jump(H, dp, N, k, buff):
            for i in range(1, N):
                # 直接跳
                for j in range(i-1, max(i-k, 0), -1):
                    if dp[j] == 1 and H[j] >= H[i]:
                        dp[i] = 1
                        break
                if dp[i] == 1:
                    continue
                # buff跳
                for j in range(i-1, max(i-k, 0), -1):
                    if buff and dp[j] == 1 and H[j] < H[i]:
                        dp[i] = 1
                        break
                    elif dp[j] == 2 and H[j] >= H[i]:
                        dp[i] = 2
                        break

            return dp[-1] == 1 or dp[-1] == 2

        T = int(input())
        for t in range(T):
            N, k = list(map(int, input().split(" ")))
            H = list(map(int, input().split(" ")))

            #init
            dp = [0] * N
            dp[0] = 1
            buff = 1

            if jump(H, dp, N, k, buff):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    t = Solution()
    t.main()