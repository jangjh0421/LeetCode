class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        for y in dict:
            while dict[y] != 1:
                nums.remove(y)
                dict[y] -= 1

        return len(dict)
