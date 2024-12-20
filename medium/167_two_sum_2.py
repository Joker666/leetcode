from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left + 1, right + 1]

            if summation > target:
                # If the sum of the numbers at the current left and right indices is greater than the target,
                # we need to decrement right to move to a smaller number
                right -= 1
            else:
                # we need to increment left to move to a larger number
                left += 1

        return []


solution = Solution()
print(solution.two_sum([2, 7, 11, 15], 9))

# I already knew this problem needs to be solved with two pointers, since it's a sorted array.
# I needed to figure out the conditionals for moving left and right.
