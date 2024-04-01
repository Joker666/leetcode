from typing import Dict


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hashmap: Dict[str, int] = {}

        for char in s:
            if hashmap.get(char) is None:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for char in t:
            if hashmap.get(char) is None:
                return False
            else:
                hashmap[char] -= 1

        for char, count in hashmap.items():
            if count != 0:
                return False
        return True


solution = Solution()
print(solution.is_anagram("anagram", "nagaram"))

# It was pretty clear I have to count the number of characters.
