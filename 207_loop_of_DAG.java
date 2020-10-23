// Version 1
// BFS + 贪心算法
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

class Solution{
    public boolean canFinish(int numCourses, int[][] prerequisites){
        if(numCourses == 0){
            return true;
        }
        // special case
        int pLen = prerequisites.length;
        if(pLen == 0){
            return true;
        }

        // init
        int[] inDegree = new int[numCourses];
        HashSet<Integer>[] adj = new HashSet[numCourses];
        for(int i=0;i<numCourses;i++){
            adj[i] = new HashSet<>();
        }

        for(int[] p: prerequisites){
            inDegree[p[0]]++;
            adj[p[1]].add(p[0]);
        }

        Queue<Integer> queue = new LinkedList<>();
        for(int i=0;i < numCourses;i++){
            if(inDegree[i] == 0){
                queue.add(i);
            }
        }
        int cnt = 0;
        while(!queue.isEmpty()){
            Integer top = queue.poll();
            cnt += 1;
            // traverse a node
            for(int successor : adj[top]){
                inDegree[successor]--;
                if(inDegree[successor]==0){
                    queue.add(successor);
                }
            }
        }
        return cnt == numCourses;
    }
}


// Version 2
// DFS + 递归回溯
// 
class Solution{

    public boolean canFinish(int numCourses, int[][] prerequisites){
        if(numCourses == 0){
            return true;
        }
        int plen = prerequisites.length;
        if(plen == 0){
            return true;
        }

        // init
        int[] marked = new int[numCourses];
        HashSet<Integer>[] graph = new HashSet[numCourses];
        for(int i=0;i<numCourses; i++){
            graph[i] = new HashSet<>();
        }
        for(int[] p:prerequisites){
            graph[p[0]].add(p[1]);
        }

        for(int i=0;i<numCourses; i++){
            if(dfs(i, graph, marked)){
                return false;
            }
        }
        // else
        return true;
    }
    /**
     * @param i      当前访问课程节点
     * @param graph
     * @param marked 1:visiting, 2:visited
     * @param return true: have loop
     */
    private boolean dfs(int i, HashSet<Integer>[] graph, int[] marked){
        if(marked[i]==1){
            // 访问中到访问中，表示遇到环
            return true;
        }

        if(marked[i]==2){
            // 访问过程没有遇到环，节点访问过
            return false;
        }
        // 遇到未搜索点
        marked[i] = 1;
        HashSet<Integer> successorNodes = graph[i];
        for(Integer successor: successorNodes){
            if(dfs(successor, graph, marked)){
                return true;
            }
        }
        // i的所有子节点已访问完成且不存在环，节点访问完成
        marked[i] = 2;
        return false;
    }
}
