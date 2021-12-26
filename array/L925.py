# https://mp.weixin.qq.com/s/zL3XDuJngAgV56i8y9Yzsw

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == 0 or len(typed) == 0:
            return False
        if name[0] != typed[0]:
            return False

        idx1 = 1
        idx2 = 1
        while idx1 < len(name) and idx2 < len(typed):
            if name[idx1] == typed[idx2]:
                idx1 += 1
                idx2 += 1

            elif typed[idx2] == name[idx1-1]:
                idx2 += 1
            else:
                return False

        if idx1 < len(name):
            return False
        while idx2 < len(typed):
            if typed[idx2] == name[idx1-1]:
                idx2 += 1
            else:
                return False
        return True


if __name__ == '__main__':
    name = "alex"
    typed = "aaleex"
    solution = Solution()

    print(solution.isLongPressedName(name, typed))