##01背包
# Version1
# 二维数组
# https://www.acwing.com/problem/content/description/2/
class Solution:
    def zeroOnePack(self):
        # input
        N, V = list(map(int, input().split()))
        C = [0]
        W = [0]
        for i in range(N):
            c, w = list(map(int, input().split()))
            C.append(c)
            W.append(w)
        
        # init
        F = [[0 for _ in range(V + 1)] for _ in range(N + 1)]
        
        # main
        for i in range(1, N + 1):  # 1:N
            for v in range(1, V + 1):  # 1:V
            	#*使用二维数组时注意更新F[i][0~C[i]]之间的状态
            	# 一维数组不用更新该部分是因为它直接覆盖掉要更新的部分，二维数组则要所有状态遍历一次
                F[i][v] = F[i-1][v]
                if v >= C[i]:
                    F[i][v] = max(F[i - 1][v], F[i - 1][v - C[i]] + W[i])
        
        print(F[N][V])


# Version2
# 一维数组
class Solution:
    def zeroOnePack(self):
        # input
        N, V = list(map(int, input().split()))
        C = [0]
        W = [0]
        for i in range(N):
            c, w = list(map(int, input().split()))
            C.append(c)
            W.append(w)
        
        # init
        F = [0 for _ in range(V + 1)]
        
        # main
        for i in range(1, N + 1):  # 1:N
        	#*V:max(Ci, V-sumiN(Ci))，体积必须逆序遍历
            for v in range(V, max(C[i], V-sum(C[i:(N+1)]))-1, -1):  
                F[v] = F[v]
                if v >= C[i]:
                    F[v] = max(F[v], F[v - C[i]] + W[i])
        
        print(F[-1])




##完全背包
# Version1
# 一维遍历+物品优化
# 使用字典对体积进行统计，然后按价值进行筛选
# 根据价值或者体积去冗余对于不同的输入有不同的效果
class Solution:
    def completePack(self):
        # input & opt
        N, V = list(map(int, input().split()))
        cnt = {}
        for i in range(N):
            c, w = list(map(int, input().split()))
            if c > V:
                continue
            if c in cnt.keys():
                cnt[c].append(w)
            else:
                cnt[c] = [w]
        #@ 更新去冗余后的物品表长
        N = len(cnt)
        
        # init
        F = [0 for _ in range(V+1)]
        C = [0]
        W = [0]
        #! 物品优化，选取价值密度大的物体：等体积大价值或等价值小体积
        for i in cnt.keys():
            C.append(i)
            W.append(max(cnt[i]))
        
        # traverse
        for i in range(1, N+1): #1:N
        	#!完全背包的体积是顺序遍历，这样才能实现重复选取同一物品的效果
            for v in range(C[i], V+1):  #Ci:V
                F[v] = max(F[v], F[v-C[i]]+W[i])
        
        print(F[-1])


## 多重背包
# Version1
# 三重循环的重复遍历
class Solution:
    def completePack(self):
        # input
        N, V = list(map(int, input().split()))

        # init
        F = [0 for _ in range(V+1)]
        C = [0]
        W = [0]
        S = [0]
        for i in range(N):
            c, w, s = list(map(int, input().split()))
            C.append(c)
            W.append(w)
            S.append(s)

        # traverse
        for i in range(1, N+1): #1:N
            #* 体积需要逆序遍历以免超出k的限度，变成完全背包
            for v in range(V, -1, -1):	
            	for k in range(1, min(S[i]+1, int(v/C[i])+1)):
                    F[v] = max(F[v], F[v-k*C[i]]+k*W[i])

        print(F[-1])
        

# Version2
# 物品优化：二进制拆分
# 定义内部方法会更加简洁，这样全局变量就不用调用self了
class Solution:
	# input shared vars
	N, V = list(map(int, input().split()))
	C = [0]
	W = [0]
	S = [0]
	F = [0 for _ in range(N+1)]
	#* opt for complete-like goods
	for i in range(N):
		c, w, s = list(map(int, input().split()))
		C.append(c)
		W.append(w)
		S.append(s)


	def zeroOnePack(self, c, w):
		# for ith goods
		for v in range(self.V, c-1, -1):
			self.F[v] = max(self.F[v], self.F[v-c]+w)

	def completePack(self, c, w):
		# for ith goods
		for v in range(c, self.V+1):
			self.F[v] = max(self.F[v], self.F[v-c]+w)

	def multiplePack(self):
		# for the whole goods 
		for i in range(1, self.N+1):
			# complete case
			if self.S[i]*self.C[i] >= self.V:
				self.completePack(self.C[i], self.W[i])
			
			# multiple case
			else:
				M = self.S[i]
				k = 1
				while k < M:
					self.zeroOnePack(k*self.C[i], k*self.W[i])
					M -= k
					k *= 2
				# for the resid coeff
				if M:
					self.zeroOnePack(M*self.C[i], M*self.W[i])

		print(self.F[-1])

# 或者没有封装函数的形式		
class Solution:

	def multiplePack(self):
		# input shared vars
		N, V = list(map(int, input().split()))
		C = [0]
		W = [0]
		S = [0]
		F = [0 for _ in range(V+1)]
		#* opt for complete-like goods
		for i in range(N):
			c, w, s = list(map(int, input().split()))
			C.append(c)
			W.append(w)
			S.append(s)

		# for the whole goods 
		for i in range(1, N+1):
			# complete case
			if S[i]*C[i] >= V:
				for v in range(C[i], V+1):
					F[v] = max(F[v], F[v-C[i]]+W[i])
			
			# multiple case
			else:
				M = S[i]
				k = 1
				while k < M:
					for v in range(V, k*C[i]-1, -1):
						F[v] = max(F[v], F[v-k*C[i]]+k*W[i])
					M -= k
					k *= 2
				# for the resid coeff
				if M:
					for v in range(V, M*C[i]-1, -1):
						F[v] = max(F[v], F[v-M*C[i]]+M*W[i])

		print(F[-1])
		
if __name__ == "__main__":
	t = Solution()
	t.multiplePack()


## 混合背包
# 加个判断就行，pass


## 二维费用背包
# 维护一维数组变为维护二维矩阵；多加一层枚举即可，pass


## 分组背包
class Solution:
    def multiGroup(self):
        # input
        N, V = list(map(int, input().split()))
        arr = []
        row = 0
        while True:
            try:
                Nk = int(input())
                arr.append([])
                for i in range(Nk):
                    arr[row].append(list(map(int, input().split())))
                row += 1
            except:
                break
        # init
        F = [0 for _ in range(V+1)]
        
        # traverse
        for g in arr:
            for v in range(V, -1, -1):
            	#！因为同组物品互斥，所以要最后一轮循环取舍，不能放在v遍历之前
                for i in g:
                    if i[0] > v:
                        continue
                    else:
                        F[v] = max(F[v], F[v-i[0]]+i[1])
        
        print(F[-1])


# 有依赖背包
# DFS，pass


# 求01背包最优方案总数
# 这里维护一维数组要更加简便些
class Solution:
    def resCnt(self):
        # input
        mod = 1e9+7    #* 防止爆int
        N, V = list(map(int, input().split()))
        C = [0]
        W = [0]
        for i in range(N):
            c, w = list(map(int, input().split()))
            C.append(c)
            W.append(w)
        
        # init
        F = [[0 for _ in range(V+1)] for _ in range(N+1)]
        Cnt = [[0 for _ in range(V+1)] for _ in range(N+1)]
        Cnt[0][:] = [1 for _ in range(V+1)]    # 不选也是一种方案，默认最优方案数应该是1
        
        # traverse
        for i in range(1, N+1):
            for v in range(V, -1, -1):
                if v >= C[i]:
                    F[i][v] = max(F[i-1][v], F[i-1][v-C[i]]+W[i])
                    if F[i][v] == F[i-1][v-C[i]]+W[i]:
                        Cnt[i][v] += Cnt[i-1][v-C[i]]
                else:
                    F[i][v] = F[i-1][v]    
                if F[i][v] == F[i-1][v]:
                    Cnt[i][v] = (Cnt[i][v] + Cnt[i-1][v]) % mod    # 防超限求模应该在每次大数相加后进行
                
        print(int(Cnt[-1][-1]))


# 输出字典序最小的方案
#!最小字典序要求给予选择低编号物品的优先权
# 而顺序状态设定(前i个物品0~i)从F[i]、F[i-1]中只能先决定i的选择，不符合要求
# 因而改变状态设定F[i]为i~N物品中的最大价值状态
# 实现上只是逆序从N~1遍历更新状态表既能实现，因为物品的编号对结果没有任何影响
# 求到最大价值后，再从F[1,V]开始回溯就能从小到大地确定最佳方案
class Solution:
    def minOrderRes(self):
        # input
        N, V = list(map(int, input().split()))
        C = []
        W = []
        for i in range(N):
            c, w = list(map(int, input().split()))
            C.append(c)
            W.append(w)
        # init
        F = [[0 for _ in range(V+1)] for _ in range(N+1)]
        res = []
        
        # Main Loop
        for i in range(N-1, -1, -1):
            for v in range(V, -1, -1):
                if v >= C[i]:
                	# 动态转移方程相应作变化
                    F[i][v] = max(F[i+1][v], F[i+1][v-C[i]]+W[i])
                else:
                    F[i][v] = F[i+1][v]
        
        # Traverse
        v = V
        for i in range(N):
            if F[i][v] == F[i+1][v-C[i]]+W[i]:
                res.append(i+1)
                v -= C[i]
        
        print(" ".join(map(str, res)))
        
