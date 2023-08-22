class Solution:
    def repeated_substring_pattern(self, s: str) -> bool:
        s_len = len(s)
        for x in range(s_len - 1):
            if s_len % (x + 1) != 0:
                continue

            substring = s[0:x+1]
            result = s.replace(substring, "")

            if result == "":
                return True

        return False


solution = Solution()
# s = "ababba" # False
# s = "babbabbabbabbab" # True
# s = "ababab" # True
# s = "abaababaab"  # True
s = "bb"  # True

print(solution.repeated_substring_pattern(s))
