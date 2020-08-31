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
			if int(s[i]) > 0 and int(s[i-1]) <= 6:		# 分类问题
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