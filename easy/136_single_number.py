from typing import Dict, List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        count_dict: Dict[int, int] = {}

        for i in range(len(nums)):
            if count_dict.get(nums[i]) is None:
                count_dict[nums[i]] = 1
            else:
                count_dict[nums[i]] += 1

        val = nums[0]
        for key in count_dict:
            if count_dict.get(key) == 1:
                return key

        return val


solution = Solution()
print(solution.single_number([4, 1, 2, 1, 2]))
