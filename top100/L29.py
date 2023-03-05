class Solution:
    def binary(self, dividend, divisor):
        if divisor > dividend:
            return 0
        total = divisor
        count = 1
        while dividend >= total+total:
            total += total
            count += count

        return count + self.binary(dividend-total, divisor)

    def divide(self, dividend: int, divisor: int) -> int:
        flag = True
        if divisor>0 and dividend<0:
            flag = False
        if divisor<0 and dividend>0:
            flag = False
        res = self.binary(abs(dividend), abs(divisor))
        if flag:
            return res
        else:
            return -res

if __name__ == '__main__':
    dividend = 10
    divisor = 3
    solution = Solution()
    print(solution.divide(dividend, divisor))