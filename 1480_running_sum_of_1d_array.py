from typing import List


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i == 0:
                continue
            nums[i] = nums[i] + nums[i - 1]

        return nums


solution = Solution()
print(solution.running_sum([3, 1, 2, 10, 1]))

# The idea is simple, update each number in place. Since it's a running sum, when we update the second element, it
# already is ready for the third element and so-and-so. We skip the first one since nothing to updat there.
