# 解读：https://mp.weixin.qq.com/s/VAMxJjoXTUxiEOJYttb6Bw

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n]*m

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]



if __name__ == '__main__':
    m = 3
    n = 7

    solution = Solution()
    print(solution.uniquePaths(m, n))