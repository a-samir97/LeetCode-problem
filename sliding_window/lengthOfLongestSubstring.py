class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = []
        start = 0
        max_ = 0

        for i in range(0, len(s)):
            se.append(s[i])
            while len(se) != len(set(se)):
                se.pop(0)
                start += 1
            max_ = max(max_, i - start + 1)
        return max_
