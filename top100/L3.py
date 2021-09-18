'''最长的不重复的子串'''
def lengthOfLongestSubstring(s):
    '''暴力'''
    max_s = ""
    for i in range(len(s)):
        tem = ""
        for j in range(i,len(s)):
            if s[j] in tem:
                break
            else:
                tem += s[j]
        if len(tem) > len(max_s):
            max_s = tem
    return len(max_s)
def lengthOfLongestSubstring2(s):
    '''滑动窗口'''
    left, right = 0, 0
    chars = set([])
    res = 0

    while right < len(s) and left <= right:
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            res = max(res,right-left)
        else:
            chars.remove(s[left])
            left += 1

    return res

def lengthOfLongestSubstring3(s):
    '''字符ascll'''
    char_index = [-1]*26
    res = 0
    left_index = 0
    for i in range(len(s)):
        index = char_index[ord(s[i])-ord('a')]
        left_index = max(index,left_index)
        res = max(res, i-left_index)
        char_index[ord(s[i])-ord('a')] = i
    return res

if __name__ == '__main__':
    print(lengthOfLongestSubstring3("pwwkew"))