# 解答：https://segmentfault.com/a/1190000017129073
# https://blog.51cto.com/u_15322551/3672067
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """从右上角开始找，每次选择一个方向"""
        if not matrix:
            return False
        row_num = len(matrix)
        col_num = len(matrix[0])
        row_index = 0
        col_index = col_num-1
        while row_index < row_num and col_index>=0:
            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] < target:
                row_index += 1
            else:
                col_index -= 1
        return False

    def _binary_search(self, matrix, target, top_left, bottom_right):
        if top_left[0]>bottom_right[0] or top_left[1]>bottom_right[1]:
            return False
        mid_x = (bottom_right[0]-top_left[0])//2 + top_left[0]
        mid_y = (bottom_right[1]-top_left[1])//2 + top_left[1]
        if matrix[mid_x][mid_y] == target:
            return True
        elif matrix[mid_x][mid_y] > target:
            # 上面，右面，下面三个区域可能
            flag1 = self._binary_search(matrix, target, top_left, (mid_x-1, mid_y-1))
            flag2 = self._binary_search(matrix, target, (mid_x, top_left[1]), (bottom_right[0], mid_y-1))
            flag3 = self._binary_search(matrix, target, (top_left[0], mid_y), (mid_x-1, bottom_right[1]))
        else:
            # 下面，右面，左面三个区域可能
            flag1 = self._binary_search(matrix, target, (top_left[0], mid_y+1), (mid_x, bottom_right[1]))
            flag2 = self._binary_search(matrix, target, (mid_x+1, top_left[1]), (bottom_right[0], mid_y))
            flag3 = self._binary_search(matrix, target, (mid_x+1, mid_y+1), bottom_right)
        return any([flag1, flag2, flag3])

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        """递归二分查找："""
        if not matrix:
            return False
        row_num = len(matrix)
        col_num = len(matrix[0])
        return self._binary_search(matrix, target, (0,0), (row_num-1, col_num-1))

if __name__ == '__main__':
    matrix = [[3,  3, 8,13,13,18],
              [4,  5,11,13,18,20],
              [9,  9,14,15,23,23],
              [13,18,22,22,25,27],
              [18,22,23,28,30,33],
              [21,25,28,30,35,35],
              [24,25,33,36,37,40]]
    target = 21
    solution = Solution()

    print(solution.searchMatrix2(matrix, target))


