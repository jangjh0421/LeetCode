class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                return True
        return False
