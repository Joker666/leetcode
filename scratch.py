from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    print(nums)

    triplets: List[List[int]] = []

    nums_len = len(nums)

    for i in range(nums_len):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = nums_len - 1

        while left < right:
            summation = nums[i] + nums[left] + nums[right]
            if summation == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif summation < 0:
                left += 1
            else:
                right -= 1

    return triplets


print(three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
