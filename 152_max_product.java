/* 30'
// Version 0
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		#init
		N = len(nums)
		# be care of negative num
		pro = None
		subpro = None

		if N == 0:
			res = []
			return res
		res = nums[0]

		for i in range(N):
			res = max(res, nums[i])
			if nums[i] != 0:
			#init
				if not pro and nums[i] > 0:
					pro = nums[i]
				elif pro and nums[i] > 0:
					pro = pro * nums[i]
					res = max(res, pro)
				else:
					pro = None

				if not subpro:
					subpro = nums[i]
				else:
					#! 错了，奇数个负数的情况下要根据最大绝对值选
					subpro = nums[i] * subpro
					res = max(res, subpro)
			
			else:
				# restart when meet 0
				pro = None
				subpro = None			

		return res
*/


// Version 1
public class Solution{
	public int maxProduct(int[] nums){
		int N = nums.length;
		if(N == 0){
			return 0;
		}

		// init
		int res = nums[0];
		int preMax = nums[0];
		int preMin = nums[0];
		int curMax;
		int curMin;

		// traverse
		for(int i=1;i<N;i++){
			if(nums[i] >= 0){
				curMax = Math.max(preMax*nums[i], nums[i]);
				curMin = Math.min(preMin*nums[i], nums[i]);
			}else{
				curMax = Math.max(preMin*nums[i], nums[i]);
				curMin = Math.min(preMax*nums[i], nums[i]);
			}
			res = Math.max(res, curMax);
			preMax = curMax;
			preMin = curMin;
		}
		return res;
	}
}