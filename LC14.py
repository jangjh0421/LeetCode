class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = strs[0]
        commonPrefix = ""
        all3 = True
        for word in strs:
            if len(word) < len(shortest):
                shortest = word

        for x in range(0, len(shortest)):
            for string in strs:
                if string[x] != shortest[x]:
                    all3 = False
            if all3:
                commonPrefix += shortest[x]

        return commonPrefix
