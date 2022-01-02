from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)

        for i in range(2, len(cost)+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        return dp[-1]




if __name__ == '__main__':
    cost = [10, 15, 20]
    solution = Solution()

    print(solution.minCostClimbingStairs(cost))