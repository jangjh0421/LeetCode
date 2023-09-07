class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for a in range(len(s)):
            if s[a] != s[len(s) - 1 - a]:
                return False

        return True
