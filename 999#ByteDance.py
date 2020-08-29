'''
# Brute Force
# input
#N = int(input())
#Map = []
#for i in range(N):
#    Map.append(list(map(int, input().split())))
N = 4
Map = [[0, 2, 6, 5], [2, 0, 4, 4], [6, 4, 0, 2], [5, 4, 2, 0]]

# init
vis = [0 for _ in range(N)]
res = 2e4

# DFS
def DFS(city, sumRes):
    curRes = 2e4
    for c in range(N):
        if not vis[c]:
            vis[c] = 1
            curRes = min(curRes, DFS(c, sumRes+Map[city][c]))
            vis[c] = 0
    return curRes if curRes != 2e4 else sumRes

for s in range(1, N):
    vis[s] = 1
    res = min(res, DFS(s, Map[0][s]))
    vis[s] = 0

print(res)


# T2
# input
T = int(input())
for t in range(T):
    N = int(input())

    # init
    curNode = set()
    res = 0
    cnt = {}
    newNode = set()

    for n in range(N):
        # one frame
        s = list(map(int, input().split()))
        k = s.pop(0)
        if k == 0:
            curNode = set()
            cnt = {}
            newNode = set()
        else:
            for i in range(k):
                x, y = s.pop(0), s.pop(0)
                newNode.add((x, y))

            for key in set.difference(curNode, newNode):
                del cnt[key]
                curNode.remove(key)

            for key in newNode:
                if key in cnt:
                    cnt[key] += 1
                else:
                    cnt[key] = 1
                res = max(res, cnt[key])
            newNode = set()

print(res)
'''


# double index
# input
N, D = list(map(int, input().split()))
arr = list(map(int, input().split()))

# init
cnt = 0
oldR = 0
r = 2

if N < 3:
    print(0)
else:
    for l in range(N-2):
        # move left
        if arr[r] - arr[l] > D:
            continue

        while arr[r] - arr[l] <= D:
            # move right
            r += 1
            if r >= N:
                break
        r -= 1
        if r == oldR:
            continue
        oldR = r
        k = r-l+1
        if k < 3:
            continue
        # update tmp
        cnt += k*(k-1)*(k-2)/6
    print(int(cnt))