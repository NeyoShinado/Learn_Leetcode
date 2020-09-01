# 数字编码
# Version 0
# 70%
def nOfStr():
    s = input().strip()
    N = len(s)

    if N == 0:
        return 0

    if s[0] == '0':
        return 0

    for i in range(1, N):
        if int(s[i-1]) == 0 and int(s[i]) == 0:
            return 0

    # init
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    dp[1] = 1

    # dp
    for i in range(1, N):
        if int(s[i-1]) <= 2 and int(s[i-1]) > 0:
            if int(s[i]) > 0 and int(s[i-1]) <= 6:      # 分类问题
                dp[i+1] = dp[i] + dp[i-1]
            elif int(s[i]) == 0:
                dp[i+1] = dp[i-1]
            else:
                dp[i+1] = dp[i]
        else:
            if int(s[i-1]) > 2 and s[i] == 0:
                return 0
            else:
                dp[i+1] = dp[i]
    return dp[-1]

print(nOfStr())

# Version1
dp = [1,1]
s = input().strip()
if s=='' or s[0]=='0': dp = [0,0]
for i in range(2, len(s) + 1):
    if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':  # 1
        dp.append(dp[i - 1] + dp[i - 2])
    elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:  # 2
        dp.append(dp[i - 2])
    elif s[i - 1] != '0':  # 3
        dp.append(dp[i - 1])
    else:
        dp.append(0)  # 4
print(dp[len(s)])


# T2
# 四个空杯装对应体积液体的最少操作步骤
def main():
    maxStep = 1000000
    vis = {}
    dp = [[0 for _ in range(maxStep)] for _ in range(6)]
    cap = list(map(int, input().split()))
    cap = [0] + cap
    finState = list(map(int, input().split()))
    finState = [6400] + finState   # 足够大的杯子
    head = 0
    tail = 0
    goalval = finState[1]*64**3 + finState[2]*64**2 + finState[3]*64**1 + finState[4]

    def movWater(waterFrom, waterTo, other1, other2, other3):
        total = dp[head][waterFrom] + dp[head][waterTo]
        dp[tail][other1] = dp[head][other1]
        dp[tail][other2] = dp[head][other2]
        dp[tail][other3] = dp[head][other3]
        dp[tail][5] = dp[head][5] + 1

        if total > cap[waterTo]:
            dp[tail][waterFrom] = total - cap[waterTo]
            dp[tail][waterTo] = cap[waterTo]
        else:
            dp[tail][waterFrom] = 0
            dp[tail][waterTo] = total

        # 将杯子状态抽象为一个值
        hashval = dp[tail][1] * 64**3 + dp[tail][2] * 64**2 + dp[tail][1] * 64 + dp[tail][4];
        if hashval == goalval:
            return dp[head][5] + 1
        if hashval not in vis:
            vis[hashval] = True
            if tail + 1 == maxStep:
                tail = 0

    # main
    if finState[1]==0 and finState[2]==0 and finState[3]==0 and finState[4]==0:
        print(str(0))
        return 0
    dp[tail][0] = 6400
    tail += 1

    try:
        while head != tail:
            if dp[head][0]:
                if finState[1]:
                    movWater(0, 1, 2, 3, 4)
                if finState[2]:
                    movWater(0, 2, 1, 3, 4)
                if finState[3]:
                    movWater(0, 3, 1, 2, 4)
                if finState[4]:
                    movWater(0, 4, 1, 2, 3)

            if dp[head][1]:
                if finState[0]:
                    movWater(1, 0, 2, 3, 4)
                if finState[2]:
                    movWater(1, 2, 0, 3, 4)
                if finState[3]:
                    movWater(1, 3, 0, 2, 4)
                if finState[4]:
                    movWater(1, 4, 0, 2, 3)
            if dp[head][2]:
                if finState[0]:
                    movWater(2, 0, 1, 3, 4)
                if finState[1]:
                    movWater(2, 1, 0, 3, 4)
                if finState[3]:
                    movWater(2, 3, 0, 1, 4)
                if finState[4]:
                    movWater(2, 4, 0, 1, 3)
            if dp[head][3]:
                if finState[0]:
                    movWater(3, 0, 1, 2, 4)
                if finState[1]:
                    movWater(3, 1, 0, 2, 4)
                if finState[2]:
                    movWater(3, 2, 0, 1, 4)
                if finState[4]:
                    movWater(3, 4, 0, 1, 2)
            if dp[head][4]:
                if finState[0]:
                    movWater(4, 0, 1, 2, 3)
                if finState[1]:
                    movWater(4, 1, 0, 2, 3)
                if finState[2]:
                    movWater(4, 2, 0, 1, 3)
                if finState[3]:
                    movWater(4, 3, 0, 1, 2)
            if head+1 == maxStep:
                head = 0
        print(str(-1))
    except e:
        print(e)

main()


# T3
# 陆地面积
def main():
    M, N = list(map(int, input().split()))
    sum = 0
    
    def link(key, x, y, set):
        