/**
# Version 0
# TC: O(2^N), SC: O(1)
# 根据每个位置上出现±的两种情况遍历2^N种方案
class Solution:
	def findTargetSumWays(self, nums: List[int], S:int) -> int:
		# init
		N = len(nums)
		res = 0

		for i in range(1, 2**N+1):
			id = 0
			summation = 0
			quotient = i
			if sum(nums[1:]) - nums[0] == S:
				res += 1
			while quotient != 1:
				resid = quotient % 2
				if resid == 1:
					summation = summation - nums[id]
				else:
					summation = summation + nums[id]
				quotient = quotient // 2
				
				if quotient == 0:
					summation = summation + sum(nums[id+1:])
				id += 1

			if summation == S:
				res += 1

		return res
**/


// Version 1
// 使用递归枚举所有排列
// 超时
// TC: O(2^N), SC: O(N) 栈空间层数
public class Solution{
	int cnt = 0;
	public int findTargetSumWays(int[] nums, int S){
		calculate(nums, 0, 0, S);
		return cnt;
	}
	public void calculate(int[] nums, int i, int sum, int S){
		if(i == nums.length){
			if(sum == S){
				cnt++;
			}
		}else{
			calculate(nums, i+1, sum+nums[i], S);
			calculate(nums, i+1, sum-nums[i], S);
		}
	}
}


// Version 2
// TC: O(N*sum), SC: O(N*sum)
// 动态规划对比枚举的优化是枝的合并
// 因为不同数的和会有重叠部分，很少出现和值完全不同的情况
// dp[i] 只与dp[i-1]有关，可以对空间进一步优化
class Solution{
	public int findTargetSumWays(int[] nums, int s){
		int sum = 0;
		int N = nums.length;
		for(int i=0;i<N;i++){
			sum += nums[i];
		}
		int[][] dp = new int[N][2*sum+1];
		dp[0][nums[0]+sum] = 1;
		dp[0][-nums[0]+sum] += 1;	// nums[0] = 0的情况要特判
		for(int i=1;i<N;i++){
			for(int j=-sum;j<=sum;j++){
				if(dp[i-1][j+sum]>0){	//!这里保证筛选由上一轮迭代的和值进行更新，保证了sum>j+nums[i]>-sum
					dp[i][j+nums[i]+sum] += dp[i-1][j+sum];
					dp[i][j-nums[i]+sum] += dp[i-1][j+sum];
				}
			}
		}
		return s>sum ? 0:dp[N-1][s+sum];
	}
} 


// Version 3
// 转化为01背包
// 所有正符号元素的和为x，负符号元素的和为y。由x+y=sum，x-y=S，即x=(S+sum)/2
// 问题转化为给定一个数组和容量为x的背包，问有多少方式装满背包
class Solution{
	public int findTargetSumWays(int[] nums, int S){
		int sum = 0;
		for(int i:nums){
			sum += i;
		}
		if((sum+S)%2==1 || S>sum){
			return 0;
		}

		int V = (sum+S)/2;
		int[] dp = new int[V+1];
		dp[0] = 1;
		for(int num:nums){
			for(int i=V;i>=num;i--){
				dp[i] += dp[i-num];
			}
		}
		return dp[V];
	}
}