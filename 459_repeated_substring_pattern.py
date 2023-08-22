class Solution:
    def repeated_substring_pattern(self, s: str) -> bool:
        substring = ""
        for x in range(len(s) - 1):
            substring = substring + s[x]
            result = s.replace(substring, "")

            if result == "":
                return True

        return False


solution = Solution()
# s = "ababba" # False
s = "babbabbabbabbab" # True
# s = "ababab" # True
# s = "abaababaab"  # True

print(solution.repeated_substring_pattern(s))
