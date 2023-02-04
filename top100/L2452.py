from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        if k == 0 or k > n:
            return 0

        max_score = float("-inf")
        for i in range(0, n-k):
            sum_value = sum(nums1[i:i+k+1])
            min_value = min(nums2[i:i+k+1])
            max_score = max(max_score, sum_value*min_value)
        return max_score


if __name__ == '__main__':
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3

    solution = Solution()
    print(solution.maxScore(nums1, nums2, k))
