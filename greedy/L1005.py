from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        neg_nums = []
        pos_nums = []

        for n in nums:
            if n>=0:
                pos_nums.append(n)
            else:
                neg_nums.append(n)

        if k == len(neg_nums):
            return sum(pos_nums) - sum(neg_nums)
        elif k > len(neg_nums):
            total = sum(pos_nums) - sum(neg_nums)
            if (k-len(neg_nums)) % 2 == 0:
                return total
            else:
                if len(neg_nums) == 0:
                    min_pos = min(pos_nums)
                    return total - min_pos * 2
                elif len(pos_nums) == 0:
                    max_neg = max(neg_nums)
                    return total + max_neg * 2
                else:
                    max_neg = max(neg_nums)
                    min_pos = min(pos_nums)
                    if abs(max_neg) < min_pos:
                        return total + max_neg * 2
                    else:
                        return total - min_pos * 2
        else:
            neg_nums.sort()
            for i in range(k):
                neg_nums[i] *= -1
            return sum(neg_nums) + sum(pos_nums)


if __name__ == '__main__':
    nums = [2,-3,-1,5,-4]
    k = 2

    solution = Solution()
    print(solution.largestSumAfterKNegations(nums, k))

