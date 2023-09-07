class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = []
        while x != 0:
            y.append(x % 10)
            x //= 10
        for a in range(len(y)):
            if y[a] != y[len(y) - 1 - a]:
                return False
        return True
