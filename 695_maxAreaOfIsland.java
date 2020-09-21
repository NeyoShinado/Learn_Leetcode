// Version 0
// BFS
import java.util.*;

class Solution{
	public int maxAreaOfIsland(int[][] grid){
		// init
		int curMax = 0;
		int M = grid.length;
		if(M==0){
			return 0;
		}
		int N = grid[0].length;
		if(N==0){
			return 0;
		}
		int cnt = 0;
		Stack<int[]> stack = new Stack<>();

		// traverse
		for(int i=0;i<M;i++){
			for(int j=0;j<N;j++){
				if(grid[i][j] != 1){
					continue;
				}else{
					stack.push(new int[]{i, j});
					grid[i][j] = -1;
					cnt += 1;
					while(!stack.empty()){
						// floodfill
						int[] node = stack.pop();
						int idx = node[0];
						int idy = node[1];
						// up
						if(idx!=0 && grid[idx-1][idy]==1){
							stack.push(new int[]{idx-1, idy});
							grid[idx-1][idy] = -1;
							cnt += 1;
						}
						// down
						if(idx!=M-1 && grid[idx+1][idy]==1){
							stack.push(new int[]{idx+1, idy});
							grid[idx+1][idy] = -1;
							cnt += 1;
						}
						// left
						if(idy!=0 && grid[idx][idy-1]==1){
							stack.push(new int[]{idx, idy-1});
							grid[idx][idy-1] = -1;
							cnt += 1;
						}
						// right
						if(idy!=N-1 && grid[idx][idy+1]==1){
							stack.push(new int[]{idx, idy+1});
							grid[idx][idy+1] = -1;
							cnt += 1;
						}
					}
					curMax = Math.max(cnt, curMax);
					cnt = 0;
				}
			}
		}
		return curMax;
	}
}


// Version 1
// 使用DFS和尾递归更快