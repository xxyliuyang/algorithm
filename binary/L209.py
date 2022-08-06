from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        slow, fast = 0, 0
        total = 0
        res = float("inf")
        flag = True
        while fast < len(nums):
            if flag:
                total += nums[fast]
            else:
                total -= nums[slow-1]

            if total >= target:
                res = min(res, fast-slow+1)
                if res == 1:
                    return res

            if total < target:
                fast += 1
                flag = True
            else:
                slow += 1
                flag = False
        if res == float('inf'):
            return 0
        else:
            return res

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        slow, fast = 0, 0
        total = 0
        res = float("inf")
        while fast < len(nums):
            while total < target and fast < len(nums):
                total += nums[fast]
                fast += 1
            while total >= target:
                res = min(res, fast-slow)
                total -= nums[slow]
                slow += 1
        if res == float('inf'):
            return 0
        else:
            return res


if __name__ == '__main__':
    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(solution.minSubArrayLen2(target, nums))