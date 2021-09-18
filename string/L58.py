class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s_list = s.strip().split(" ")

        if s_list[-1]:
            return len(s_list[-1])
        else:
            return 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("abs "))
