class Solution:
    def __init__(self):
        self.symbol_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        self.append_symbol = "([{"
        self.pop_symbol = ")]}"

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.append_symbol:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                prec = stack.pop()
                if self.symbol_dict[prec] != c:
                    return False
        return len(stack) == 0

if __name__ == '__main__':
    s = "()[]{}"
    solution = Solution()
    print(solution.isValid(s))