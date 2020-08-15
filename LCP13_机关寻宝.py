# LCP13 机关寻宝
# Version0
# 有死循环
class Solution:
    def minimalSteps(self, maze) -> int:
        # init
        res = float("inf")
        Os = []
        Ms = []
        dist = {}  # tuple eles

        if maze == [] or maze == [[]]:
            print(-1)
        rows = len(maze)
        cols = len(maze[0])

        # key loc traverse
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == "S":
                    S = (i, j)
                elif maze[i][j] == "T":
                    T = (i, j)
                elif maze[i][j] == "O":
                    Os.append((i, j))
                elif maze[i][j] == "M":
                    Ms.append((i, j))

        # BFS build dist
        def BFS(start, end):
            # start, end is the loc_tuple of the maze
            endX, endY = end
            dist = -1
            queue = [(start, 0)]
            vis = [[0 for _ in range(cols)] for _ in range(rows)]

            while queue:
                node, cnt = queue.pop(0)
                x, y = node
                vis[x][y] = 1
                if x == endX and y == endY:
                    return cnt
                # udlr
                if x - 1 >= 0 and vis[x - 1][y] != 1 and maze[x - 1][y] != "#":
                    queue.append(((x - 1, y), cnt + 1))
                if x + 1 < rows and vis[x + 1][y] != 1 and maze[x + 1][y] != "#":
                    queue.append(((x + 1, y), cnt + 1))
                if y - 1 >= 0 and vis[x][y - 1] != 1 and maze[x][y - 1] != "#":
                    queue.append(((x, y - 1), cnt + 1))
                if y + 1 < cols and vis[x][y + 1] != 1 and maze[x][y + 1] != "#":
                    queue.append(((x, y + 1), cnt + 1))

            # no way
            return -1

        # res1 no M
        if len(Ms) == 0:
            res = BFS(S, T)
            print(res)
            return

        for o in Os:
            dist[(S, o)] = BFS(S, o)
            for m in Ms:
                if (m, T) not in dist:
                    dist[(m, T)] = BFS(m, T)
                dist[(m, o)] = BFS(m, o)
                dist[(o, m)] = dist[(m, o)]

        # DFS min Cost
        # 负无穷距离可用于剪枝，最后距离记得转型
        tmp = {"Cur": S, "T": T, "O": Os, "M": Ms, "n": 0}
        stack = [tmp]
        while stack:
            tmp = stack.pop()

            # S stage
            if tmp["Cur"] == S:
                loc = tmp["Cur"]
                for o in tmp["O"]:
                    if dist[(S, o)] == -1:
                        continue
                    else:
                        tmp["Cur"] = o
                        tmp["n"] += dist[(S, o)]
                        stack.append(tmp)
                        # 回溯
                        tmp["Cur"] = loc
                        tmp["n"] = 0

            # M stage
            # pop 1 loc one time
            elif tmp["Cur"] in tmp["O"]:
                for i in len(tmp["M"]):
                    o = tmp["Cur"]
                    m = tmp["M"].pop(i)
                    n = tmp["n"]
                    if dist[(o, m)] == -1:
                        continue
                    else:
                        tmp["Cur"] = m
                        tmp["n"] += dist[(o, m)]
                        stack.append(tmp)
                        # 回溯
                        tmp["Cur"] = o
                        tmp["n"] = n
                        tmp["M"].insert(i, m)

            # O stage
            elif tmp["Cur"] in tmp["M"] and tmp["M"]:
                for o in tmp["O"]:
                    m = tmp["Cur"]
                    n = tmp["n"]
                    if dist[(m, o)] == -1:
                        continue
                    else:
                        tmp["Cur"] = o
                        tmp["n"] += dist[(m, o)]
                        stack.append(tmp)
                        # 回溯
                        tmp["Cur"] = m
                        tmp["n"] = n

            # T stage
            else:
                m = tmp["Cur"]
                n = tmp["n"]
                if dist[(m, T)] == -1:
                    continue
                else:
                    tmp["n"] += dist[(m, T)]
                    res = min(res, tmp["n"])

        if res == float("inf"):
            print(-1)
        else:
            print(res)


if __name__ == "__main__":
    maze = ["S#O", "M..", "M.T"]
    t = Solution()
    t.minimalSteps(maze)