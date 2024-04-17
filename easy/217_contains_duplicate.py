from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


solution = Solution()
print(solution.contains_duplicate([1, 2, 3, 11]))
