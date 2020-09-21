// Version 1
// 动态编程
// 水坑中的水深是由最低边界确定的
// 两次扫描，找出水坑中左右端的最高边界
class Solution{
	public int trap(int[] height){
		if(height==null || height.length==0){
			return 0;
		}
		int res = 0;
		int N = height.length;
		int[] maxL = new int[N];
		int[] maxR = new int[N];
		maxL[0] = height[0];
		for(int i=1;i<N;i++){
			maxL[i] = Math.max(height[i], maxL[i-1]);
		}
		maxR[N-1] = height[N-1];
		for(int i=N-2;i>=0;i--){
			maxR[i] = Math.max(height[i], maxR[i+1]);
		}
		for(int i=1;i<N-1;i++){
			res += Math.min(maxL[i], maxR[i]) - height[i];
		}
		return res;
	}
}


// Version 2
// 单调栈
// 栈中存放下标以计算宽度，每出现高值就将栈元素抛出，更新体积
class Solution{
	public int trap(int[] height){
		int res = 0;
		int cur = 0;
		int N = height.length;
		Stack<Integer> st = new Stack<Integer>();
		while(cur<N){
			while(!st.empty() && height[cur]>height[st.peek()]){
				int sentiel = st.peek();
				st.pop();
				if(st.empty()){
					break;
				}
				int width = cur - st.peek() - 1;
				int high = Math.min(height[cur], height[st.peek()]) - height[sentiel];
				res += width * high;
			}
			st.push(cur++);
		}
		return res;
	}
}


// Version 3
// 双指针
// 以递归的角度看，水坑的水深是由最外层的边界中的最小值确定的
// 即从两端向中间遍历时，更新较小值边界那个水坑的体积是肯定不会有错的
class Solution{
	public int trap(int[] height){
		int l = 0, r = height.length-1;
		int res = 0;
		int maxL = 0, maxR = 0;
		while(l < r){
			if(height[l] < height[r]){
				if(height[l] > maxL){
					maxL = height[l];
				}else{
					res += maxL - height[l];
				}
				++l;
			}else{
				if(height[r] > maxR){
					maxR = height[r];
				}else{
					res += maxR - height[r];
				}
				--r;
			}
		}
		return res;
	}
}
