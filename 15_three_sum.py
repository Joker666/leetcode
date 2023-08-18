from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        intermediate = {}
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
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res = [nums[i], nums[left], nums[right]]
                    result.append(res)
                    left += 1

        return result


solution = Solution()
arr = [-1, 0, 1, 2, -1, -4]
s = solution.three_sum_2(arr)
print("\n\n")
print(s)
# Output: [[-1,-1,2],[-1,0,1]]
