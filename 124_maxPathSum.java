/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */


// Version 0
// recursion
// 每一个子树有六种选择方案
class Solution{
	public int maxPathSum(TreeNode root){
		int L=Integer.MIN_VALUE;
		int R=Integer.MIN_VALUE;
		int sum;
		int res;

		res = root.val;
		if(root.left!=null){
			// 返回的不是节点最大路径和，而是该子树里的最大路径和，所以结果不正确
			L = maxPathSum(root.left);
			res = Math.max(L, res);
			sum = L + root.val;
			res = Math.max(sum, res);
		}
		if(root.right!=null){
			R = maxPathSum(root.right);
			res = Math.max(R, res);	
			sum = R + root.val;
			res = Math.max(sum, res);
		}
		if(root.left!=null && root.right!=null){
			// 无法解决初速化报错
			sum = L + R + root.val;
			res = Math.max(sum, res);
		}
		return res;
	}
}


// Version 1
// 返回最大子路径同时更新子节点为根的子路径和
// TC: O(N), SC: O(N)
class Solution{
	int maxSum = Integer.MIN_VALUE;	// 有负数的场景初始化为最小值

	public int maxPathSum(TreeNode root){
		maxGain(root);
		return maxSum;
	}

	public int maxGain(TreeNode node){
		if(node==null){
			return 0;
		}

		// 计算左右子树的最大增益路径
		int leftGain = Math.max(maxGain(node.left), 0);
		int rightGain = Math.max(maxGain(node.right), 0);

		// 更新选取当前节点路径的最大路径和
		int priceNewPath = node.val + leftGain + rightGain;
		maxSum = Math.max(maxSum, priceNewPath);

		return node.val + Math.max(leftGain, rightGain);
	}
}