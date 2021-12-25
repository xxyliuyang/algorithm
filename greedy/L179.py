from typing import List

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        tmp = sorted(map(str, nums), key=LargerNumKey)
        tmp = "".join(tmp)
        if tmp.startswith("0"):
            return "0"
        else:
            return tmp
if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    solution = Solution()

    print(solution.largestNumber(nums))