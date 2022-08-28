import copy

class Solution():
    def __init__(self):
        self.path = []
        self.result = []
        self.sub_s = ""
    def backtrack(self, s, start):
        if start == len(s):
            self.result.append(copy.deepcopy(self.path))
            return

        for i in range(start, len(s)):
            self.sub_s = self.sub_s + s[i]
            if not self.check_p(self.sub_s):
                continue
            self.path.append(self.sub_s)
            self.sub_s = ""
            self.backtrack(s, i + 1)
            self.sub_s = self.path.pop()

    def check_p(self, sub_s):
        if sub_s == sub_s[::-1]:
            return True
        return False

    def partition(self, s: str):
        if len(s) == 0:
            return []
        self.backtrack(s, 0)
        return self.result

if __name__ == '__main__':
    s = "efe"
    solution = Solution()
    print(solution.partition(s))