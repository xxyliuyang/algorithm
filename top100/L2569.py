from typing import List


class Solution:
    def update_with_flag1(self, nums, l, r):
        for i in range(l, r+1):
            nums[i] = 1 if nums[i] == 0 else 0

    def update_with_flag2(self, nums1, nums2, p):
        for i in range(len(nums2)):
            nums2[i] += nums1[i] * p

    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for flag, v1, v2 in queries:
            if flag == 1:
                self.update_with_flag1(nums1, v1, v2)
            elif flag == 2:
                self.update_with_flag2(nums1, nums2, v1)
            else:
                res.append(sum(nums2))
        return res


if __name__ == '__main__':
    nums1 = [1, 0, 1]
    nums2 = [0, 0, 0]
    queries = [[1, 1, 1], [2, 1, 0], [3, 0, 0]]

    solution = Solution()
    print(solution.handleQuery(nums1, nums2, queries))
