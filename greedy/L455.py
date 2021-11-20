from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        s_idx, g_idx = 0, 0
        count = 0
        while g_idx < len(g):
            if s_idx >= len(s):
                break
            if g[g_idx] <= s[s_idx]:
                count += 1
                s_idx += 1
            g_idx += 1
        return count


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]

    solution = Solution()
    print(solution.findContentChildren(g, s))