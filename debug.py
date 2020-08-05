#! usr/etc/bin python
#coding: utf-8

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