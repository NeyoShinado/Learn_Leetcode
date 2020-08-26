# T1
# 游戏裁判
# 70%
def playGames():
	# input
	N = int(input())
	nums = list(map(int, input().split()))

	# init
	maxRound = max(nums)
	refRound = maxRound*(N-1) - sum(nums)
	res = maxRound

	while refRound < res:
		refRound += N-1
		res += 1
	return res

print(playGames())
	

# T2
# 排列规划
def main():
    mod = 1000000007
    N = int(input())
    flags = list(map(int, input().strip().split()))
    dp = [[0 for _ in range(N+1)] for _ in range(N)]
    for i in range(N):
        dp[0][i] = 1
 
    for i in range(1, N):
        if flags[i-1] == 1:
            for j in range(N-i-1, -1, -1):
                dp[i][j] += dp[i-1][j+1] + dp[i][j+1]
                dp[i][j] %= mod
        else:
            dp[i][0] += dp[i-1][0]
            dp[i][0] %= mod
            for j in range(1, N-i):
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
                dp[i][j] %= mod
    # print(dp)
    print(dp[N-1][0] % mod)
 
 
if __name__ == '__main__':
    main()


# T3
# 红篮球进阶
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner reader = new Scanner(System.in);
    while (reader.hasNext()) {
      System.out.printf("%.5f", new Main().solution(reader.nextInt(), reader.nextInt()));
    }
  }

  private double solution(int n, int m) {
    double[][] dp = new double[n + 1][m + 1];
    for (int i = 1; i <= n; i++) {
      dp[i][0] = 1.0;
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        dp[i][j] += (double) i / (i + j);
        if (j > 1) {
          dp[i][j] += (double) j / (i + j) * (j - 1) / (i + j - 1) * i / (i + j - 2) * dp[i - 1][j - 2];
        }
        if (j > 2) {
          dp[i][j] += (double) j / (i + j) * (j - 1) / (i + j - 1) * (j - 2) / (i + j - 2) * dp[i][j - 3];
        }
      }
    }
    return dp[n][m];
  }
}