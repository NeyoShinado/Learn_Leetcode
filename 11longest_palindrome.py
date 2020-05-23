'''
# Vesrion1
# 回文情况的枚举
# TC:  SC:O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # init
        length = 0
        dist = 0
        biase = 0
        N = len(s)
        D = {}
        res = ""

        if len(set(s)) == 1:
            return s

        if len(s) == 0:
            return s

        # search palindrome loc
        for id in range(0, N):
            if s[id] == s[id-1] and id > 0:  # palindrome begin
                biase = -1        # biase between head & tail
                if D.__contains__("loc"):
                    D["loc"].append(id)
                    D["biase"].append(biase)
                else:
                    D["loc"] = [id]
                    D["biase"] = [biase]

            if s[id] == s[id-2] and id > 1:    # "sooos"
                biase = -2
                if D.__contains__("loc"):
                    D["loc"].append(id)
                    D["biase"].append(biase)
                else:
                    D["loc"] = [id]
                    D["biase"] = [biase]


        # count palindrome
        if D.__contains__("loc"):
            N_palin = len(D["loc"])
            for id in range(N_palin):
                i = D["loc"][id]
                biase = D["biase"][id]
                while s[i] == s[i - dist + biase]:
                    if length < dist-biase+1:
                        res = s[(i-dist+biase):(i+1)]
                        length = len(res)
                    dist = dist + 2
                    i = i + 1
                    if (i-dist+biase) < 0 or i > (N-1):
                        break
                dist = 0
        else:
            # not 'aba' or 'bb' format palindrome
            return s[0]
        

        return res
# test case
# "ccd"
# "sooos"
'''

'''
# Version2
# Brute Force
# TC:O(N^3)  SC:O(1)
class Solution:
    def longestPalindrome(self, s):
        if len(set(s)) == 1:
            return s

        N = len(s)
        if N < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(N-1):
            for j in range(i+1, N):
                 if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j+1]

        return res

    def __valid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
'''

'''
# Version3
# 动态规划
# 拆解回文判断为①首尾字符相等和②子字符串是否为回文的判断
# TC:O(N^2)  SC:O(N^2)
class Solution:
    def longestPalindrome(self, s):
        N = len(s)

        if N < 2:
            return s

        # 标记回文的上三角矩阵
        dp = [[False for _ in range(N)] for _ in range(N)]
        length = 1
        id = 0    # 返回回文起始索引

        for i in range(N):
            dp[i][i] = True

        for j in range(1, N):
            for i in range(j-1, -1, -1):
                # 回文判断
                if s[i] == s[j]:    # 先判断首尾字符是否相等
                    if j-i < 3:    # 引用子字符串的边界条件
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False


                # 回文长度对比
                if dp[i][j] and (j-i+1) > length:
                    length = (j-i+1)
                    id = i

        return s[id, id+length]
'''


# Version 4
# Manacher algorithm
