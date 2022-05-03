
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if n == 0:
            return m
        if m == 0:
            return n

        dp = [[0 for _ in range(n)] for _ in range(m)]
        if word1[0] != word2[0]:
            dp[0][0] = 2

        flag = dp[0][0] == 0
        for i in range(1, m):
            if word1[i] == word2[0] and not flag:
                dp[i][0] = dp[i-1][0] - 1
                flag = True
            else:
                dp[i][0] = dp[i-1][0] + 1
        flag = dp[0][0] == 0
        for i in range(1, n):
            if word2[i] == word1[0] and not flag:
                dp[0][i] = dp[0][i - 1] - 1
                flag = True
            else:
                dp[0][i] = dp[0][i - 1] + 1

        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j-1]+2, dp[i-1][j]+1, dp[i][j-1]+1])
        return dp[m-1][n-1]

    def minDistance2(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if n == 0:
            return m
        if m == 0:
            return n

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j-1]+2, dp[i-1][j]+1, dp[i][j-1]+1])
        return dp[m][n]

    def minDistance3(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [0 for _ in range(n+1)]
        for i in range(m+1):
            tmp = [0 for _ in range(n+1)]
            for j in range(n+1):
                if i == 0 or j == 0:
                    tmp[j] = i+j
                elif word1[i-1] == word2[j-1]:
                    tmp[j] = dp[j-1]
                else:
                    tmp[j] = min([dp[j-1]+2, dp[j]+1, tmp[j-1]+1])
            dp = tmp
        return dp[-1]

if __name__ == '__main__':
    word1 = "sea"
    word2 = "eat"

    solution = Solution()
    print(solution.minDistance3(word1, word2))