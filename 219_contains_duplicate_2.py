from typing import List, Dict


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        hashmap: Dict[int, int] = {}
        for index, num in enumerate(nums):
            if num in hashmap and index - hashmap[num] <= k:
                return True
            hashmap[num] = index
        return False


solution = Solution()
solution.contains_nearby_duplicate([1, 2, 3, 1], 3)
