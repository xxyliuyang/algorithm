from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_result = []
        if len(nums) == 0:
            return product_result

        product_result.append(1)
        for i in range(1, len(nums)):
            product_result.append(product_result[i-1]*nums[i-1])

        p = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            product_result[i] *= p
            p *= nums[i]
        return product_result

if __name__ == '__main__':
    solution = Solution()
    nums = [-1]
    print(solution.productExceptSelf(nums))