package LeetCode;

public class IslandPerimeter {

    public static void main(String[] args){
        int[][] grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
        System.out.println(test(grid));
    }


    public static int test(int[][] grid){
        // 从左上开始遍历，新加入的陆地只考虑上方和左方的情况
        // ①一块相邻，res+2；②两块相邻，res不变
        // init
        int res = 0;
        int M = grid.length;
        int N = grid[0].length;
        int state = 0;

        for (int i=0; i<M; i++){
            for (int j=0; j<N; j++){
                // meet land
                if (grid[i][j] == 1){
                    state = 0;
                    if (i>0){
                        state += grid[i-1][j];
                    }
                    if (j>0){
                        state += grid[i][j-1];
                    }
                    if(state == 0) {
                        res += 4;
                    }else if(state == 1){
                        res += 2;
                    }
                }
            }
        }
        return res;
    }
}
