from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_numbers = [0]
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                is_vowel = 1
            else:
                is_vowel = 0
            vowel_numbers.append(vowel_numbers[i] + is_vowel)

        result = []
        for left, right in queries:
            vowel_number = vowel_numbers[right+1] - vowel_numbers[left]
            result.append(vowel_number)
        return result

if __name__ == '__main__':
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]]
    solution = Solution()
    print(solution.vowelStrings(words, queries))
