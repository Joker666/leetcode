from typing import List


class Solution:
    # is_palindrome_2 reverses the string
    def is_palindrome(self, x: int) -> bool:
        string_num = str(x)
        string_num_array = [*string_num]
        self.reverse(string_num_array, 0, len(string_num_array) - 1)

        return string_num == "".join(string_num_array)

    # is_palindrome_2 reverses the number
    def is_palindrome_2(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit

            num = num // 10

        return x == reversed_num

    def reverse(self, text: List[str], left: int, right: int):
        if left > right:
            return
        text[left], text[right] = text[right], text[left]
        self.reverse(text, left + 1, right - 1)


solution = Solution()
s = solution.is_palindrome_2(121)
print(s)

# I actually made a string and reversed it to get it right.
# Then I learned this pattern that you can reverse a number by taking remainders
# and then diving it.
