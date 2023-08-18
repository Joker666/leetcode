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


solution = Solution()
arr = [3, 0, -2, -1, 1, 2]
s = solution.three_sum(arr)
print("\n\n")
print(s)
# Output: [[-1,-1,2],[-1,0,1]]
