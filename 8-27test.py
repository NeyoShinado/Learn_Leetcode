class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        if K != 2 and N % (K-1) != 1:
            return -1
        if N == 0:
            return 0

