// Version0
// 加入列、主对角、副对角状态的逐行深度优先搜索
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;


public class test{
	private int n;
	private boolean[] col;
	private boolean[] sub;
	private boolean[] main;
	private List<List<String>> res;
	
	public List<List<String>> NQueens(int n){
		res = new ArrayList<>();
		if(n == 0) {
			return res;
		}
		
		this.n = n;
		this.col = new boolean[n];
		this.sub = new boolean[2*n-1];
		this.main = new boolean[2*n-1];
		Deque<Integer> path = new ArrayDeque<>();
		dfs(0, path);
		return res;
	}
	
	private void dfs(int row, Deque<Integer> path) {
		if(row == n) {
			List<String> board = convert2board(path);
			res.add(board);
			return;
		}
		
		// 尝试是否可以放置
		for(int j=0;j<n;j++) {
			if(!col[j] && !sub[row+j] && !main[row-j+n-1]) {
				path.addLast(j);
				col[j] = true;
				sub[row+j] = true;
				main[row-j+n-1] = true;
				
				dfs(row+1, path);
				
				main[row-j+n-1] = false;
				sub[row+j] = false;
				col[j] = false;
				path.removeLast();
			}
		}
	}
	private List<String> convert2board(Deque<Integer> path){
		List<String> board = new ArrayList<>();
		for (Integer num:path) {
			StringBuilder row = new StringBuilder();
			row.append(".".repeat(Math.max(0,  n)));
			row.replace(num,  num+1,  "Q");
			board.add(row.toString());
		}
		return board;
	}
}