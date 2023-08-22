class Solution:
    def repeated_substring_pattern(self, s: str) -> bool:
        s_len = len(s)
        for x in range(1, s_len // 2 + 1):
            if s_len % x != 0:
                continue

            substring = s[0:x]
            full_string = substring * (s_len // x)

            if s == full_string:
                return True

        return False


solution = Solution()
# s = "ababba" # False
s = "babbabbabbabbab" # True
# s = "ababab" # True
# s = "abaababaab"  # True
# s = "bb"  # True

print(solution.repeated_substring_pattern(s))
