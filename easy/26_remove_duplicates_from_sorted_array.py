from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        num_len = len(nums)

        if num_len <= 1:
            return num_len

        curr = 0
        then = 1
        while then < num_len:
            if nums[curr] == nums[then]:
                then = then + 1
            else:
                nums[curr + 1] = nums[then]
                curr = curr + 1

        return curr + 1


solution = Solution()
solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])


# The complexity here is updating the array in-place.
# It was not clear to me even tho I had prior knowledge that sorted array problems are most
# likely a two pointer problem. The hints gave me idea that a fast-slow pointer can help with
# swapping the values.
