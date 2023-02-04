from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        res = sorted(score, key=lambda x: x[k], reverse=True)
        return res

if __name__ == '__main__':
    score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    solution = Solution()
    print(solution.sortTheStudents(score, 2))