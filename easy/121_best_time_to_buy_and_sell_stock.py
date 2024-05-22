from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        max_diff = 0
        minimum = 0
        for i in range(1, len(prices)):
            if i == 1:
                minimum = min(prices[i - 1], prices[i])
            else:
                minimum = min(minimum, prices[i])
            diff = prices[i] - minimum
            if diff > max_diff:
                max_diff = diff
        return max_diff

    def max_profit_2(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            else:
                if profit > max_profit:
                    max_profit = profit
            right += 1
        return max_profit


solution = Solution()
print(solution.max_profit_2([2, 1, 2, 1, 0, 1, 2]))
# print(solution.max_profit_2([7, 1, 5, 3, 6, 4]))


# This one I couldn't solve without a bit of hint that once I get the minimum value and I can keep track of it
# and check for maximum diff with the minimum value.

# However, this is inherently a sliding window problem. A two-pointer solution is more intuitive. We can initialize
# two pointers and update the left pointer anytime we get the minimum and right pointer keeps progressing.
