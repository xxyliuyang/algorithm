#https://mp.weixin.qq.com/s?__biz=MzUxNjY5NTYxNA==&mid=2247494448&idx=2&sn=08f97a245ce1110a704d0d6051338922&scene=21#wechat_redirect
from typing import List
import copy

class Solution:
    def __init__(self):
        self.result = []
        self.path = []
    def backtrack(self, target, k, sum_v, start_index):
        if sum_v > target:
            return
        if sum_v == target and len(self.path) == k:
            self.result.append(copy.deepcopy(self.path))
            return

        for i in range(start_index, 10):
            self.path.append(i)
            self.backtrack(target, k, sum_v+i, i+1)
            self.path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(n, k, 0, 1)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))