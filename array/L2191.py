from typing import List

class Solution:

    def get_index(self, mapping, num):
        index = ""
        for a in num:
            index += str(mapping[int(a)])
        return int(index)

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        index_map = [self.get_index(mapping, str(num)) for num in nums]
        num_indexs = list(zip(index_map, nums))
        num_indexs.sort(key=lambda x:x[0])
        return [n_i[1] for n_i in num_indexs]

if __name__ == '__main__':
    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = [991,338,38]

    solution = Solution()
    print(solution.sortJumbled(mapping, nums))