class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        l = 0
        res = 0

        for h in range(len(s)):
            while s[h] in freq:
                freq.remove(s[l])
                l += 1
            freq.add(s[h])
            res = max(res, h - l + 1)
        
        return res