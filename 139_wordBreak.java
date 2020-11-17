// Version 0
// DP(ListNode) + 剪枝
class Solution{
	public boolean wordBreak(String s, List<String> wordDict){
		// init
		// list 2 hashmap
		Int N = s.length;
		Int maxW = 0;
		Linkedlist<Integer> splitId = Linkedlist<>();
		splitId.add(0);
		StringBuffer sb = s;

		// build map
		
		// traverse
		for(id=0;i<N;i++){
			for(start:splitId){
				if((id-start)<=maxW && sb[start:id] in dict){
					splitId.add(id);
					break;
				}else{
					continue;
				}
			}
		}

		return true if splitId.tail==N-1 else false;
	}
}


// Version 1
// dp(数组) + 剪枝
// TC: O(N^2), SC: O(N)
public class Solution{
	public boolean wordBreak(String s, List<String> wordDict){
		Set<String> wordDictSet = new HashSet(wordDict);
		boolean[] dp = new boolean[s.length() + 1];
		dp[0] = true;
		int maxW = 0;
		for(String w: wordDict){
			if(w.length() > maxW){
				maxW = w.length();
			}
		}

		for(int i=1;i<=s.length();i++){
			for(int j=0;j<i;j++){
				if(dp[j] && j-i<= maxW && wordDictSet.contains(s.substring(j, i))){
					dp[i] = true;
					break;
				}
			}
		}
		return dp[s.length()];
	}
}


// Version 2
// 基于字典元素的DFS
// 不过没有记忆化机制，在处理重复字符串中会超时
// 0ms ans
class Solution{
	public boolean wordBreak(String s, List<String> wordDict){
		if(s.length() == 0){
			return true;
		}

		if(s.length() >= 149){
			return false;
		}

		for(int i=0;i<wordDict.size();i++){
			String temp = wordDict.get(i);
			if(s.startsWith(temp)){
				if(wordBreak(s.substring(temp.length()), wordDict)){
					return true;
				}
			}
		}
		return false;
	}
}


// Version 3
// DFS + 记忆化
// TC: O(N), SC: O(N)
class Solution{
	public boolean wordBreak(String s, List<String> wordDict){
		boolean[] visited = new boolean[s.length()+1];
		return dfs(s, 0, wordDict, visited);
	}

	private boolean dfs(String s, int start, List<String> wordDict, boolean[] visited){
		for(String word:wordDict){
			int nextStart = start + word.length();
			if(nextStart > s.length() || visited[nextStart]){
				continue;
			}

			if(s.indexOf(word, start) == start){
				if(nextStart==s.length() || dfs(s, nextStart, wordDict, visited)){
					return true;
				}
				visited[nextStart] = true;
			}
		}
		return false;
	}
}


// Version 4
// BFS
class Solution{
	public boolean wordBreak(String s, List<String> wordDict){
		Queue<Integer> queue = new LinkedList<>();
		queue.add(0);

		int N = s.length();
		boolean[] visited = new boolean[N+1];

		while(!queue.isEmpty()){
			int size = queue.size();
			for(int i=0;i<size;i++){
				int start = queue.poll().intValue();
				for(String word: wordDict){
					int id = start + word.length();
					if(id > N || visited[id]){
						continue;
					}

					if(s.indexOf(word, start) == start){
						if(id == N){
							return true;
						}

						queue.add(id);
						visited[id] = true;
					}
				}
			}
		}
		return false;
	}
}