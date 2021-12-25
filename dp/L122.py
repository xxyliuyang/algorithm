# https://mp.weixin.qq.com/s?__biz=MzUxNjY5NTYxNA==&mid=2247495978&idx=2&sn=4f0c25539bbd1734f01c9bec0c0c5b3c&scene=21#wechat_redirect

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0]*len(prices) # 买股票后的现金
        dp2 = [0]*len(prices) # 卖股票后的现金
        if len(prices) < 2:
            return 0
        dp1[0] -= prices[0]
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i-1], dp2[i-1]  - prices[i])
            dp2[i] = max(dp2[i-1], dp1[i-1] + prices[i])
        return max(dp1[-1], dp2[-1])



if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))