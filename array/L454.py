from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_12 = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                sum_12[n1+n2] += 1

        result = 0
        for n3 in nums3:
            for n4 in nums4:
                result += sum_12.get(0-n3-n4, 0)
        return result

    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        freq_a = {}
        freq_b = {}
        freq_c = {}
        freq_d = {}
        for i in range(0, len(nums1)):
            freq_a[nums1[i]] = freq_a.get(nums1[i], 0) + 1

        for i in range(0, len(nums2)):
            freq_b[nums2[i]] = freq_b.get(nums2[i], 0) + 1

        for i in range(0, len(nums3)):
            freq_c[nums3[i]] = freq_c.get(nums3[i], 0) + 1

        for i in range(0, len(nums4)):
            freq_d[nums4[i]] = freq_d.get(nums4[i], 0) + 1

        freq_a_b = {}
        for i in freq_a.keys():
            for j in freq_b.keys():
                freq_a_b[i + j] = freq_a_b.get(i + j, 0) + freq_a[i] * freq_b[j]

        freq_c_d = {}
        for i in freq_c.keys():
            for j in freq_d.keys():
                freq_c_d[i + j] = freq_c_d.get(i + j, 0) + freq_c[i] * freq_d[j]

        for i in freq_a_b.keys():
            j = -i
            if freq_c_d.get(j, None) is not None:
                count = count + (freq_a_b[i] * freq_c_d[j])

        return count


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(solution.fourSumCount2(nums1, nums2, nums3, nums4))
