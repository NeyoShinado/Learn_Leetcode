// Version 1
// 将哈希表设置为数组
// 通过正负标记表示是否出现，第一轮将负数标为N+1，第二轮将1~N范围的下标索引值为负
class Solution{
	public int firstMissingPositive(int[] nums){
		int n = nums.length;
		for(int i=0;i<n;++i){
			if(nums[i]<=0){
				nums[i] = n+1;
			}
		}
        for(int i=0;i<n;++i){
            int num = Math.abs(nums[i]);
            if(num<=n){
				nums[num-1] = -Math.abs(nums[num-1]);
			}
        }

		// output
		for(int i=0;i<n;++i){
			if(nums[i]>0){
				return i+1;
			}
		}
		return n+1;
	}
}


// Version 2
// 遍历一次，通过换位的方法使得元素出现在对应的位置上
// 分三种情况讨论：①元素正序出现num[i]=i+1；②元素不合法
// num[i]>N or num[i]<=0 or num[i]=num[num[i]-1]吻合位置重复出现时，交换会导致死循环；
// ③num[i]∈[1,N]，则将其放回正确的位置；
public class test{
	public static int firstMissingPositive() {
		// init
		int[] nums = {3, 4, -1, 1};
		int N = nums.length;
		int l = 0;
		int r = N;

		for(int i=0;i<N;++i) {
			while(nums[i]>0 && nums[i]<=N && nums[nums[i]-1]!=nums[i]) {
				int tmp = nums[nums[i]-1];
				nums[nums[i]-1] = nums[i];
				nums[i] = tmp;
			}
		}
		for (int i=0;i<N;i++) {
			if(nums[i] != i+1) {
				return i+1;
			}
		}
		return N+1;
	}
	public static void main(String[] args) {
		System.out.println(firstMissingPositive());
	}
}
