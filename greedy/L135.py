# 讲解：https://mp.weixin.qq.com/s/9IX4GM3BTxMS_ATBigW97A
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0

        candies = [0] * len(ratings)
        candies[0] = 1
        for i in range(len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
            else:
                candies[i] = 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] +1, candies[i])
        return sum(candies)

if __name__ == '__main__':
    ratings = [1,0,2]
    solution = Solution()

    print(solution.candy(ratings))
