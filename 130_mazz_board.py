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


# Version1
# DFS递归
import sys
sys.setrecursionlimit(10000000)
class Solution:
    def solve(self, board):
        def dfs(i, j):
        # dfs 尽量使用全局变量，减少大数据的递归传输
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "X" or board[i][j] == "#":
            # 越界或已阅
                return
            board[i][j] = '#'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        if board == [] or board == [[]]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in [0, n-1]:
                dfs(i, j)

        for i in [0, m-1]:
            for j in range(n):
                dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == '#':
                    board[i][j] = 'O'


# Version2
# DFS非递归
#!这里要遍历完一个点的近邻(上下左右)才把该点出栈
class Solution:
    def solve(self, board):
        def dfs(i, j):
            cands = []
            board[i][j] = '#'
            cands.append([i, j])

            #udlr
            while cands:
                # 未遍历完所有近邻点不弹出当前点
                x, y = cands[-1]
                if x-1 >= 0 and board[x-1][y] == 'O':
                    cands.append([x-1, y])
                    board[x-1][y] = '#'
                    continue
                if x+1 < m and board[x+1][y] == 'O':
                    cands.append([x+1, y])
                    board[x+1][y] = '#'
                    continue
                if y-1 >= 0 and board[x][y-1] == 'O':
                    cands.append([x, y-1])
                    board[x][y-1] = '#'
                    continue
                if y+1 < n and board[x][y+1] == 'O':
                    cands.append([x, y+1])
                    board[x][y+1] = '#'
                    continue

                cands.pop()


        if board == [] or board == [[]]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


