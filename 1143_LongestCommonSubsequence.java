// Version 0
// DP
class Solution{
	public int longestCommonSubsequence(String text1, String text2){
		char[] s1 = text1.toCharArray();
		char[] s2 = text2.toCharArray();
		int N = s1.length;
		int M = s2.length;
		int[][] dp = new int[N+1][M+1];

		for(int i=1;i<N+1;i++){
			for(int j=1;j<M+1;j++){
				if(s1[i-1]==s2[j-1]){
					dp[i][j] = dp[i-1][j-1]+1;
				}else{
					dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
				}
			}
		}
		return dp[N][M];
	}
}