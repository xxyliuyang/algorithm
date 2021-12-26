
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap1 = {}
        cmap2 = {}

        for i in range(len(s)):
            if s[i] not in cmap1:
                cmap1[s[i]] = t[i]
            if t[i] not in cmap2:
                cmap2[t[i]] = s[i]
            if cmap1[s[i]] != t[i] or cmap2[t[i]] != s[i]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))