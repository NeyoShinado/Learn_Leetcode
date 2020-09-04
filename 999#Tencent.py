# T7
# EyeGaurd
def eyeCnt():
    # 贪心思想
    N, L = list(map(int, input().split()))
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr = sorted(arr, key=lambda x:x[0])

    # init
    res = 0
    r = 0
    l = 0
    # can not cover left edge
    if arr[0][0] > l:
        return -1

    # l <= i & r max
    while r < L:
        if not arr:
            return -1
        if arr[0][0] > l:
            l = r
            res += 1
        eye = arr.pop(0)
        if eye[1] > r:
            r = eye[1]
        if eye[1] >= L:
            return res+1

print(eyeCnt())