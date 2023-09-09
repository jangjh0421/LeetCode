class Solution(object):
    def plusOne(self, digits: list[int]) -> any:

        digits[-1] += 1
        for x in range(1, len(digits) + 1):
            if digits[-x] == 10:
                digits[-x] = 0
                try:
                    digits[- (x + 1)] += 1
                except IndexError:
                    digits = [1] + digits
            else:
                break
        return digits
