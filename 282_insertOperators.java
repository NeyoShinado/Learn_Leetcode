// Version 1
// 递归枚举 + 优先运算回溯

class Solution{
	public ArrayList<String> res;
	public String s;
	public long target;

	public void recurse(int id, long pre, long cur, long value, ArrayList<String> ops){
		String nums = this.s;

		// Done and return
		if(id == nums.length()){
			if(value == this.target && cur == 0){	//*cur 不等于0时扩展阶段的表达式，不完整的
				StringBuilder sb = new StringBuilder();
				ops.subList(1, ops.size()).forEach(v -> sb.append(v));    //*remove first term "+" [1, size)
				this.res.add(sb.toString());
			}
			return;
		}

		// Extend ops -- insert""
		cur = cur * 10 + Character.getNumericValue(nums.charAt(id));
		String curValRep = Long.toString(cur);
		int N = nums.length();

		// Avoid preNum-subNum: like 054
		if(cur > 0){
			recurse(id+1, pre, cur, value, ops);
		}

		// insert "+"
		ops.add("+");
		ops.add(curValRep);
		recurse(id+1, cur, 0, value+cur, ops);
		// Backtrack for "-" & "*"
		ops.remove(ops.size()-1);
		ops.remove(ops.size()-1);

		if(ops.size() > 0){		// *要以+号起始
			// insert "-"
			ops.add("-");
			ops.add(curValRep);
			recurse(id+1, -cur, 0, value-cur, ops);
			// Backtrack
			ops.remove(ops.size()-1);
			ops.remove(ops.size()-1);
			// insert "*"
			ops.add("*");
			ops.add(curValRep);
			recurse(id+1, cur*pre, 0, value-pre+(cur*pre), ops);	//*前缀乘积放入pre实现累乘
			// Backtrack
			ops.remove(ops.size()-1);
			ops.remove(ops.size()-1);
		}
	}

	public List<String> addOperators(String num, int target){
		res = new ArrayList<String>();
		if(num.length()==0){
			return res;
		}
		this.target = target;
		this.s = num;
		this.res = res;
		this.recurse(0, 0, 0, 0, new ArrayList<String>());
		return this.res;
	}
}


// Version 2
// 思路和上述一样
// 优化在于插入""的元素扩展部分通过while循环实现
// 这样开辟的递归层数(N)比起Version1 逢扩展就传进递归递归层数(N^2)要更少，速度自然就更快
class Solution{
	public List<String> addOperators(String num, int target){
		List<String> res = new ArrayList<>();
		char[] expr = new char[2 * num.length()];
		dfs(num, expr, 0, 0, 0, 0, target, res);
		return res;
	}

	public void dfs(String num, char[] expr, int len, long pre, long val, int id, int target, List<String> res){
		// 递归结束
		if(id == num.length()){
			if(val == target){
				res.add(new String(expr, 0, len));
			}
			return;
		}

		long cur = 0;
		int s = id;		// 记录当前元素位于字符串的位置
		int l = len;	// 记录当前表达式起始位置
		if(s!=0)++len;	// 初始化填充
		while(id<num.length()){		//!维持s不变实现插入""功能
			cur = cur*10+num.charAt(id)-'0';
			if(num.charAt(s)=='0' && id-s>0){	// 排除前导0元素
				break;
			}
			if(cur>Integer.MAX_VALUE) break;
			expr[len] = num.charAt(id);
			len++;
			id++;
			if(s == 0){
				dfs(num, expr, len, n, n, id, target, res);
				continue;
			}
			expr[l] = '+';
			dfs(num, expr, len, n, val+n, id, target, res);
			expr[l] = '-';
			dfs(num, expr, len, -n, val-n, id, target, res);
			expr[l] = '*';
			dfs(num, expr, len, pre*n, val-pre+pre*n, id, target, res);
		}
	}
}