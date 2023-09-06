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
s = "babbabbabbabbab"  # True
# s = "ababab" # True
# s = "abaababaab"  # True
# s = "bb"  # True

print(solution.repeated_substring_pattern(s))

# Even though this should be an easy problem, it took me several attempts. My first intuition was
# storing character counts and reducing if the character is found, eventually if all character counts
# were zero, we found substring pattern. This didn't work since characters can be sorted differently.

# Second intuition was to go upto the middle and check left and right, if they match substring pattern.
# However, this approach also didn't work since not always we will have substrings that repeat upto the center.

# Third intuition came from cody that we iterate and find the smallest substring and try matching it.
# I used string replace which was slower, but it got accepted.

# It was a terrible solution and I had to look up editorial to find out that all substrings length will
# be divisor of the full length, and you can skip the other ones. Also, there's no need to replace all
# substrings, you can make the full string as you know the divisor number.
