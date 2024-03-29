from typing import Dict, List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_dict: Dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return [nums_dict[nums[i]], i]
            else:
                diff = target - nums[i]
                nums_dict[diff] = i


solution = Solution()
s = solution.two_sum([2, 7, 11, 15], 22)
print(s)

# Initially I did it in two loops.
# What I found intuitive was that I had the idea of diffing but didn't tackle that.
# Ultimately the diff and extra memory solves the problem.
