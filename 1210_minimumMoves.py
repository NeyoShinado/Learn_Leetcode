# Version 0
# TLE
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # init
        s = 0    # 四个状态:0,90,180, 270
        N = len(grid)
        node = (0, 0)
        cnt = 0
        queue = [[node, s]]
        nextQueue = []
        
        # BFS
        while queue:
            node, s = queue.pop(0)
            x, y = node

            if s == 0:
                # right
                if y+2 < N and grid[x][y+2] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 0])
                    if newNode == (N-1, N-2):
                        return cnt
                # down
                if x+1 < N and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 0])
                    if newNode == (N-1, N-2):
                        return cnt
                # spin right
                if x < N-1 and grid[x+1][y] | grid[x+1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 3])
                # spin left
                if x > 0 and grid[x-1][y] | grid[x-1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 1])

            elif s == 1:
                # right
                if y+1 < N and grid[x][y+1] | grid[x-1][y+1] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 1])
                # down
                if x+1 < N and grid[x+1][y] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 1])
                # spin right
                if y < N-1 and grid[x-1][y+1] | grid[x][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 0])
                    if newNode == (N-1, N-2):
                        return cnt
                # spin left
                if x > 0 and grid[x-1][y] | grid[x-1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 1])
                    if newNode == (N-1, N-1):
                        return cnt
            elif s == 2:
                # right
                if y+1 < N and grid[x][y+1] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 2])
                    if newNode == (N-1, N-1):
                        return cnt
                # down
                if x+1 < N and grid[x+1][y] | grid[x+1][y-1] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 2])
                    if newNode == (N-1, N-1):
                        return cnt
                # spin right
                if x > 0 and grid[x-1][y] | grid[x-1][y-1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 2])
                # spin left
                if x < N-1 and grid[x+1][y] | grid[x+1][y-1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 3])
            else:
                # right
                if y < N-1 and grid[x][y+1] | grid[x+1][y+1] == 0:
                    newNode = (x, y+1)
                    nextQueue.append([newNode, 3])
                # down
                if x+2 < N and grid[x+2][y] == 0:
                    newNode = (x+1, y)
                    nextQueue.append([newNode, 3])
                # spin right
                if y < N-1 and grid[x][y+1] | grid[x+1][y+1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 0])
                # spin left
                if y > 0 and grid[x][y-1] | grid[x+1][y-1] == 0:
                    newNode = (x, y)
                    nextQueue.append([newNode, 2])

            if not queue:
                cnt += 1
                queue = nextQueue.copy()
                nextQueue = []