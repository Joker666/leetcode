from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return digits

        num = 0

        for i in range(len(digits)):
            num = (num * 10) + digits[i]

        num = num + 1
        return_digits: List[int] = []

        while num != 0:
            return_digits.append(num % 10)
            num = num // 10

        return_digits.reverse()
        return return_digits

    def plus_one_2(self, digit: List[int]) -> List[int]:
        for i in range(len(digit) - 1, -1, -1):
            if digit[i] == 9:
                digit[i] = 0
            else:
                digit[i] += 1
                return digit

        digit.append(0)
        digit[0] = 1
        return digit


solution = Solution()
s = solution.plus_one_2([9, 9, 9, 9])
print(s)

# I took the basic approach first to find the number from the array and add 1 and generating result array
# A smarter solution is just incrementing the last digit and handling if there's 9
# The only time it will fail if there's all 9s and that case can be handled as well
