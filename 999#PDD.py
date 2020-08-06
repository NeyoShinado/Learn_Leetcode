### 2018年
#------------------------------------------------- 
#T1：商品翻页显示系统
# 两个商品列表，根据已阅商品offset和当前页商品数n返回展示商品在列表中的提取区间。


#T2: 拼多多王国装路灯
#!usr/etc/bin/ python
# **utf-8**
# DFS 正解
from collections import defaultdict


limit = int(input())
city = int(input())
tree = defaultdict(lambda :dict())
parent = {}
visited = {}
root = None

# build tree
for _ in range(city - 1):
    s = input().split()
    u, v, d = int(s[0]), int(s[1]), int(s[2])
    if d > limit:
        continue
    if not root:
        root = u
    parent[v] = u
    tree[u][v] = d

# find root
while parent.get(root, -1) != -1:
    root = parent.get(root)
    
'''
cand：候选队列，存放当前节点的所有可能路径长度
children：存放以当前节点为根节点的所有的子节点
sets：存放以当前节点为根节点的子树下，每个孩子节点的候选队列
'''
def dfs(u):
    if u not in visited:
        cand = set()
        cand.add(0)
        if u in tree:
            sets = []
            children = []
            for v in tree[u]:
                children.append(v)
                sets.append(dfs(v))
            for i in range(len(sets)):
                d = tree[u][children[i]]
                for c in sets[i]:
                    if d + c <= limit:
                        cand.add(d + c)
                for j in range(i + 1, len(sets)):
                    d2 = tree[u][children[j]]
                    for c in sets[i]:
                        for c2 in sets[j]:
                            if c + c2 + d + d2 <= limit:
                                cand.add(c + c2 + d + d2)
        visited[u] = cand
    return visited[u]


print(max(dfs(root)))

# BFS错解
import sys
class Solution:

    def max_led(self):
        # init
        graph = {}      # dict {cityA:{cityB:road}}
        link_cities = set()     # linked cities

        # input
        max_road = int(input())
        N = int(input())
        #max_road = 9
        #N = 5
        #matrix = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4]]
        #for i in matrix:
        #    ca, r, cb = i
        for i in sys.stdin:
            ca, cb, r = list(map(int, i.split(" ")))
            link_cities.add(ca)
            link_cities.add(cb)
            if ca in graph:
                graph[ca][cb] = r
            else:
                graph[ca] = {cb:r}
            if cb in graph:
                graph[cb][ca] = r
            else:
                graph[cb] = {ca:r}

        def BFS(queue):
        # 树状结构保证了城与城之间没有环形结构，visited都为1的城不能再相连
            res = 0
            visited = [0] * N
            while queue:
                (city, curRoad) = queue.pop(0)
                if visited[city] == 2:
                    continue
                # record cur_city's visited time
                curCityvisit = visited[city]
                for newCity, newRoad in graph[city].items():
                    # visited check
                    if (visited[city] == 1 and visited[newCity] == 1) or visited[newCity] == 2:
                        continue

                    if curRoad+newRoad > max_road:
                        continue
                    elif curRoad+newRoad == max_road:
                        return max_road

                    queue.append((newCity, curRoad+newRoad))
                    res = max(res, curRoad+newRoad)
                    visited[newCity] += 1
                    if curCityvisit == visited[city]:
                        visited[city] += 1

                # 注意首都有路时visited[0] != 0，否则弃用更新
            if 0 in link_cities and visited[0] == 0:
                res = None

            return res


        # start BFS
        # check if capical is linked
        #if 0 in link_cities:
        #    res = BFS([(0, 0)])
        #else:
        res = 0
        for city in link_cities:
            tmp = BFS([(city, 0)])
            if tmp:
                res = max(res, tmp)

        print(res)


if __name__ == "__main__":
    t = Solution()
    t.max_led()


# T3: 最大三乘数
#!usr/etc/bin/ python
#coding: utf-8
import sys
class Solution:

    def maxThreePro(self):
        # input
        N = int(input())
        nums = list(map(int, input().split(" ")))
        #N = 4
        #nums = [3, 4, 1, 2]
        if N < 3:
            return

        # init
        res = 0
        pro = []        # three/one max neg eles for pos_res
        zero = False
        neg_max = []    # three max neg eles for neg_res
        neg_min = []    # two min neg eles for pos_res

        for i in range(N):
            if nums[i] > 0:
                if not pro:
                    pro.append(nums[i])
                else:
                    for index in range(len(pro)):
                        if nums[i] <= pro[index]:
                            pro.insert(index, nums[i])
                        if index == len(pro)-1 and nums[i] > pro[index]:
                            pro.append(nums[i])
                # delete eles if > 3
                if len(pro) > 3:
                    pro.pop(0)
            elif nums[i] < 0:
                # 负元素先入max 再入min
                if not neg_max and not neg_min:
                    neg_max.append(nums[i])
                elif neg_max and not neg_min:
                    for index in range(len(neg_max)):
                        if nums[i] <= neg_max[index]:
                            neg_max.insert(index, nums[i])
                        if index == len(neg_max)-1 and nums[i] > neg_max[index]:
                            neg_max.append(nums[i])
                    if len(neg_max) > 3:
                        neg_min.append(neg_max.pop(0))
                else:
                    if nums[i] <= neg_min[-1]:
                        for index in range(len(neg_min)):
                            if nums[i] <= neg_min[index]:
                                neg_min.insert(index, nums[i])
                            if nums[i] > neg_min[index] and index == len(neg_min)-1:
                                neg_min.append(nums[i])
                        if len(neg_min) > 2:
                            neg_min.pop(-1)

                    elif nums[i] > neg_min[-1] and nums[i] <= neg_max[0]:
                        if len(neg_min) == 2:
                            continue
                        else:
                            neg_min.append(nums[i])
                    else:
                        for index in range(len(neg_max)):
                            if nums[i] <= neg_max[index]:
                                neg_max.insert(index, nums[i])
                            if index == len(neg_max)-1 and nums[i] > neg_max[index]:
                                neg_max.append(nums[i])
                        if len(neg_max) > 3:
                            neg_max.pop(0)

            else:
                zero = True

        # res Summary
        if (len(pro) >= 1 and len(neg_min) == 2):
            res = max(res, pro[-1]*neg_min[0]*neg_min[1])
        if len(pro) >= 3:
            res = max(res, pro[0]*pro[1]*pro[2])
            print(res)
            return
        if zero:
            print(0)
            return
        print(neg_max[0]*neg_max[1]*neg_max[2])


if __name__ == "__main__":
    t = Solution()
    t.maxThreePro()


# T4
# 小熊抢糖
# 二元数组排序


### 2019年
#-------------------------------------------------
# T1 靓号修改
# Tag：贪心；字符串

# T2 间隔植树⭐
# Tag: 回溯；剪枝
# 陷阱：按顺序排列可能会陷入前期耗尽小数目的品种，导致后期数目大的品种无法分割开。因此必须右回溯步骤。
# 另，若某一种类的数目超过N/2，就要剪枝，削减计算成本。

# AC
import sys
sys.setrecursionlimit(10000000)
#input
N = int(input())
arr = list(map(int, input().split()))
M, res = sum(arr), []

def DFS(arr, m, preTree):
    # m 为当前剩下树的数目
    global res
    if m == 0:
        return True
    for i in range(len(arr)):
        tree = i+1
        if arr[i] * 2 > m+1:
            return False
        if arr[i] > 0 and preTree != tree:
            arr[i] -= 1
            res.append(tree)
            if DFS(arr, m-1, tree):
                retunr True
            # 子树不符合则回溯处理
            res.pop(-1)
            arr[i] += 1
    return False
if def(arr, M, 0):
    print(" ".join(map(str, res)))
else:
    print("-")

# Version0
# 直接按顺序分割排列，Not pass
class Solution:
    def plantTrees(self):
        # input
        N = int(input())
        trees = list(map(int, input().split(" ")))


        if N == 1 and trees[0] > 1:
            print("-")
            return

        t1 = 0
        t2 = 1
        index = 2
        res = []

        while (trees[t1] > 0 and trees[t2] > 0) or (trees[t1] ^ trees[t2]) == 1:
            # plant tree
            if trees[t1] > 0:
                res.append(t1+1)
                trees[t1] -= 1
            if trees[t2] > 0:
                res.append(t2+1)
                trees[t2] -= 1

            # tree empty
            if trees[t1] == 0 and index < N:
                t1 = index
                index += 1
            if trees[t2] == 0 and index < N:
                t2 = index
                index += 1

        # resid check
        if trees[t1] == 0 and trees[t2] == 0:
            print(" ".join(list(map(str, res))))
        else:
            print("-")

if __name__ == "__main__":
    t = Solution()
    t.plantTrees()


# T3 偶数数组两两配对组合中，最小的（最大和-最小和）
# Tag：贪心，排序，哈希
# 贪心的思路十分直观，最大值和最小值依次配对，和的分布也会尽量平均（可用反证法证明）


# Version0
# 爆内存
class Solution:
    def minSub(self):
        # input
        N = int(input())
        nums = list(map(int, input().split(" ")))
        #nums = [2, 6, 4, 3]
        res = []
        ans = []

        # init
        queue = [[nums, []]]

        # BFS
        while queue:
            tmp = queue.pop(0)
            cands = tmp[0]
            sums = tmp[1]
            # no more nodes, save the ans
            if len(cands) == 0:
                ans.append(sums)

            for i in range(len(cands)):
                for j in range(i+1, len(cands)):
                    newSums = sums.copy()
                    newCands = cands.copy()
                    node1 = newCands[i]
                    node2 = newCands[j]
                    newCands.pop(j)    # 有序情况下，从后往前删除不会导致索引错位
                    newCands.pop(i)
                    newSums.append(node1+node2)
                    queue.append([newCands, newSums])

        # res Summary
        for sums in ans:
            res.append(max(sums) - min(sums))

        print(str(min(res)))


if __name__ == "__main__":
    t = Solution()
    t.minSub()
