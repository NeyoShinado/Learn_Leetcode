// Version 1
// Hash
// 逆序情况下性能仍然不高
class Solution{
	public int longestConsecutive(int[] nums){
		// init
		Set<Integer> numSet = new HashSet<>();
		for(int num: nums){
			numSet.add(num);
		}

		int res = 0;

		for(int num: nums){
			if(!numSet.contains(num-1)){
				int currentNum = num;
				int currentStreak = 1;

				while(numSet.contains(currentNum+1)){
					currentNum += 1;
					currentStreak += 1;
				}
				res = Math.max(currentStreak, res);
			}
		}
		return res;
	}
}


// Version 2
// Hash + 两端查询
// 解决了Version 1一个方向查询的缺点
// TC: O(N), SC: O(N)
class Solution{
	public int longestConsecutive(int[] nums){
		int n = nums.length;
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		int res = 0;
		for(int num: nums){
			if(!map.containsKey(num)){
				int left = map.get(num-1)==null ? 0 : map.get(num-1);
				int right = map.get(num+1)==null ? 0 : map.get(num+1);

				int curLen = 1+left+right;
				if(curLen > res){
					res = curLen;
				}
				map.put(num, curLen);
				map.put(num-left, curLen);
				map.put(num+right, curLen);
			}
		}
		return res;
	}
}


// Version 3
// 并查集
// #1 递归
// TC: O(N^2), SC: O(N)
class Solution{
	public int find(int x, Map<Integer, Integer> map){
		return map.containsKey(x)? find(x+1, map) : x;
	}

	public int longestConsecutive(int[] nums){
		Map<Integer, Integer> map = new HashMap<>();
		for(int i=0;i<nums.length; i++){
			// 通过哈希表构建并查集
			map.put(nums[i], i);
		}
		int max = 0;
		for(int i:nums){
			max = Math.max(max, find(i+1, map) - i);
		}
		return max;
	}
}
// #2 迭代
// 通过并查集去重 + Version 1的子序列优化遍历的冗余
class Solution{
	public int find(int x, Map<Integer, Integer> map){
		return map.containsKey(x)? find(x+1, map): x;
	}

	public int longestConsecutive(int[] nums){
		Map<Integer, Integer> map = new HashMap<>();
		for(int i=0; i<nums.length; i++){
			map.put(nums[i], i);
		}

		int max = 0;
		for(int num:nums){
			if(!map.containsKey(num-1)){
				max = Math.max(max, find(num+1, map)-num);
			}
		}
		return max;
	}
}