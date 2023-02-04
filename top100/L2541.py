
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1

        n = len(nums1)
        add_steps = 0
        sub_steps = 0
        for i in range(n):
            v = abs(nums1[i]-nums2[i])
            if v % k != 0:
                return -1
            if nums1[i] > nums2[i]:
                sub_steps += v // k
            else:
                add_steps += v // k
        if add_steps == sub_steps:
            return add_steps
        else:
            return -1

if __name__ == '__main__':
    nums1 = [4, 3, 1, 4]
    nums2 = [1, 3, 7, 1]
    k = 3

    solution = Solution()
    print(solution.minOperations(nums1, nums2, k))