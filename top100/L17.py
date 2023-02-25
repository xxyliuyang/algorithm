from typing import List

class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.digit_letter_dict = {
            "0": [""],
            "1": [""],
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

    def backtrack(self, digits, index):
        if index == len(digits):
            self.result.append("".join(self.path))
            return

        for c in self.digit_letter_dict[digits[index]]:
            self.path.append(c)
            self.backtrack(digits, index + 1)
            self.path.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.backtrack(digits, 0)
        return self.result


if __name__ == '__main__':
    digits = "23"
    solution = Solution()
    print(solution.letterCombinations(digits))