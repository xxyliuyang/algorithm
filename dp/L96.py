# https://mp.weixin.qq.com/s/dWleWATSrJJF6gahJr6UCg

class Solution:


    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            next_val = 0
            for j in range(1, i+1):
                left_count = j - 1
                right_count = i - j
                next_val += dp[left_count] * dp[right_count]
            dp[i] = next_val
        return dp[-1]

if __name__ == '__main__':
    n = 3
    solution = Solution()

    print(solution.numTrees(n))