# 讲解：https://mp.weixin.qq.com/s/-m0ZmZJhWIJxdU3i4nlPSQ
# 局部最优：遇到 strNum [i - 1] > strNum [i] 的情况，让 strNum [i - 1]--，然后 strNum [i] 给为 9，可以保证这两位变成最大单调递增整数
# 全局最优：得到小于等于 N 的最大单调递增的整数。

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digit_str = str(n)
        result = [int(i) for i in digit_str]
        flag = len(result)
        for i in range(len(result)-2, -1, -1):
            if result[i] > result[i+1]:
                result[i] = result[i]-1
                flag = i+1
        for i in range(flag, len(result)):
            result[i] = 9
        result = [str(i) for i in result]
        return int("".join(result))


if __name__ == '__main__':
    solution = Solution()
    print(solution.monotoneIncreasingDigits(100))