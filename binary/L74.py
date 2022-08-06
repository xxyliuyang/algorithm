from typing import List
class Solution:
    def find_row(self, matrix, target):
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_col(self, row, target):
        left = 0
        right = len(row)
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return mid
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row_index = self.find_row(matrix, target)
        if row_index == -1:
            return False
        col_index = self.find_col(matrix[row_index], target)
        if col_index == -1:
            return False
        else:
            return True

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    solution = Solution()
    print(solution.searchMatrix(matrix, target))