class Solution:
    M = 10 ** 9 + 7

    def qpow(self, x, y):
        r = 1
        while y > 0:
            if y & 1:
                r = (r * x) % self.M
            x = (x * x) % self.M
            y = y >> 1
        return r

    def monkeyMove(self, n: int) -> int:
        res = self.qpow(2, n) - 2
        if res < 0:
            res = res + self.M
        return res


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.monkeyMove(n))
