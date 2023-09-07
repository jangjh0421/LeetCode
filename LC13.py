class Solution:
    def romanToInt(self, s: str) -> int:
        rt = 0
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        for i in range(0, len(s)):
            if i == len(s)-1 or dict[s[i]] >= dict[s[i+1]]:
                rt += dict[s[i]]
            else:
                rt -= dict[s[i]]
        return rt
