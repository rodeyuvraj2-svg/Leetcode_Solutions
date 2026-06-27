class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
                reverse = int(str(x)[::-1])

                if x == reverse:
                    return True
                else:
                    return False