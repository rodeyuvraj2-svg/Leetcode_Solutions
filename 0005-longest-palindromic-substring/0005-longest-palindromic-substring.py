class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def expand_from_center(l,r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):

            odd = expand_from_center(i,i)
            even = expand_from_center(i,i+1)

            res = max(res,odd,even, key=len)

        return res