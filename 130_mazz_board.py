# Version0
# DFS边界搜索
import sys
sys.setrecursionlimit(10000000)

class Solution:
    def solve(self, mazz: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # global vars init
        if len(mazz)==0 or len(mazz[0])==0:
            return
        H = len(mazz)
        W = len(mazz[0])
        visited = [[0 for _ in range(W)] for _ in range(H)]

        def DFS(i, j):
            if visited[i][j] != 0 or mazz[i][j] == 'X':
                return
            if mazz[i][j] == 'O':
                visited[i][j] = 1
            else:
                visited[i][j] = -1
            
            # up
            if i != 0:
                DFS(i-1, j)
            # down
            if i != H-1:
                DFS(i+1, j)
            # left
            if j != 0:
                DFS(i, j-1)
            # right
            if j != W-1:
                DFS(i, j+1)

        # DFS on the boundary
        for i in range(H):
            DFS(i, 0)
            DFS(i, W-1)
        for j in range(W):
            DFS(0, j)
            DFS(H-1, j)

        # traverse res
        for i in range(H):
            for j in range(W):
                if visited[i][j] != 1:
                    mazz[i][j] = 'X'
        