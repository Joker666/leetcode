from typing import List


class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                total = total + accounts[i][j]

            if total > maxi:
                maxi = total

        return maxi


solution = Solution()
print(solution.maximum_wealth([[1, 5], [7, 3], [3, 5]]))
