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


# 跳桩
#! usr/etc/bin python
#coding: utf-8
# DFS
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