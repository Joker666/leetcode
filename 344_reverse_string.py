from typing import List


class Solution:
    def reverse_string(self, text: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(text, 0, len(text) - 1)

    def reverse(self, text: List[str], left: int, right: int):
        if left > right:
            return

        text[left], text[right] = text[right], text[left]
        self.reverse(text, left + 1, right - 1)


solution = Solution()
s = ["H", "a", "n", "n", "a", "h"]
print(s)
solution.reverse_string(s)
print(s)

# Even though I got it right the first time,
# it took a bit of time to find the pattern of left and right
