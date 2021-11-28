# 讲解：https://mp.weixin.qq.com/s/nzP0hKD7kOvPxIOKKi5mBQ
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0
        total_sum = 0
        start = 0

        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            cur_sum += gas[i] - cost[i]

            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        if total_sum < 0:
            return -1
        else:
            return start


if __name__ == '__main__':
    gas = [2,3,4]
    cost = [3,4,3]

    solution = Solution()
    print(solution.canCompleteCircuit(gas, cost))