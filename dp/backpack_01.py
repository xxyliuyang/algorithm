# 解读1：https://mp.weixin.qq.com/s/bSSRPsur9Yfm73LBcdRNPw
# 解读2：https://mp.weixin.qq.com/s/B-jK6vclyrV5BCGTW1BkfA

from typing import List

class Solution:
    def two_wei_dp(self, bag_weight: int, weight: List[int], value: List[int]) -> int:
        """
        dp[i][j]: 包重量j，前i个物品可以获取的最大价值
        """
        dp = [[0 for _ in range(bag_weight + 1)] for _ in range(len(weight))]

        for j in range(bag_weight):
            dp[0][j] = value[0] if j >= weight[0] else 0

        for i in range(1, len(weight)):
            for j in range(1, bag_weight+1):
                if j < weight[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i]] + value[i])

        return dp[len(weight)-1][bag_weight]

    def one_wei_dp(self, bag_weight: int, weight: List[int], value: List[int]) -> int:
        """
        dp[j]: 包重量j, 可以获取的最大价值
        """
        dp = [0 for _ in range(bag_weight + 1)]

        for i in range(len(weight)):
            for j in range(bag_weight, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

        return dp[bag_weight]



if __name__ == '__main__':
    solution = Solution()
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    print(solution.two_wei_dp(bag_weight, weight, value))
    print(solution.one_wei_dp(bag_weight, weight, value))