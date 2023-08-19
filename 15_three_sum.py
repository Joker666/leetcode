from typing import List, Dict, Tuple


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        intermediate: Dict[Tuple[int, int], int] = {}
        result: List[List[int]] = []

        for x in range(len(nums)):
            for y in range(len(nums)):
                if x == y:
                    continue

                intermediate[x, y] = nums[x] + nums[y]

        for x in range(len(nums)):
            for keys, value in intermediate.items():
                if x in keys:
                    continue

                if nums[x] + value != 0:
                    continue

                res = [nums[x], nums[keys[0]], nums[keys[1]]]
                res.sort()

                if res in result:
                    continue
                result.append(res)

        return result

    def three_sum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                summation = nums[i] + nums[left] + nums[right]

                if summation < 0:
                    left += 1
                elif summation > 0:
                    right -= 1
                else:
                    res = [nums[i], nums[left], nums[right]]
                    result.append(res)
                    left += 1

        return result


solution = Solution()
arr = [-1, 0, 1, 2, -1, -4]
s = solution.three_sum(arr)
print(s)
# Output: [[-1,-1,2],[-1,0,1]]


# First intuition was three loops which is not ideal
# Second tried to store the pair of two number indices in a dictionary and
# then computing the third index from that
# Since it was open to the duplicate triplet issue, I sorted the triplet list and
# Checked if it already exists in the final list or not
# It worked, but it failed in "Time limit exceeded" for such a poor solution

# The second intuition is to use set and two sum to calculate, but I did not pursue that
# I have solved that in 2021 with some help maybe

# The third intuition I had was using two pointers, but I forgot how to go about that
# Using one loop to go from left to right and then a nested one with two pointers
# can solve the issue. One pointer would move from left and another from right. The question is
# what condition will make the pointers move? Turns out to *zero* in on the target 0, if a sum is
# greater than 0, we should move the right pointer to left and if it is lower than 0 then the left
# pointer to the right.
# This solves the pointer movement but still fails on the duplicate triplet issue.
