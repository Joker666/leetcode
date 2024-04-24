from typing import Dict


class Solution:
    def tribonacci(self, n: int) -> int:
        return self.traverse(n, {})

    def traverse(self, n: int, my_dict: Dict[int, int]) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        if n in my_dict:
            return my_dict[n]

        val = self.traverse(n - 1, my_dict) + self.traverse(n - 2, my_dict) + self.traverse(n - 3, my_dict)

        my_dict[n] = val
        return val


solution = Solution()
print(solution.tribonacci(14))
