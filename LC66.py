class Solution:
    def plusOne(self, digits: list[int]) -> any:
        dig = digits[0]
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] += 1

        elif len(digits) == 1 and digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            for x in range(len(digits)-1, -1, -1):
                if x == 0:
                    if digits[x] == 10 or digits[x] == 9:
                        if dig == 9:
                            digits[x] = 0
                            digits.insert(0, 1)
                    else:
                        digits[x] += 1

                elif digits[x] == 10 or digits[x] == 9:
                    digits[x] = 0
                    digits[x - 1] += 1

        return digits
