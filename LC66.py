class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[len(digits)-1] == 9:
            if len(digits) == 1:
                digits[0] = 1
                digits.append(0)
            else:
                if (digits[len(digits)-2] + 1) > 9:
                    if len(digits) - 3 == -1:
                        digits.insert(0, 1)
                    else:
                        digits[len(digits) - 3] += 1

                    digits[len(digits) - 2] = 0
                digits[len(digits)-1] = 0
        else:
            digits[len(digits)-1] += 1
        return digits
