from typing import Dict, List, Optional


def repeated_substring_pattern(s: str) -> bool:
    for i in range(len(s) // 2):
        substring = s[0:i + 1]
        full_string = substring * (len(s) // (i+1))
        if full_string == s:
            return True

    return False


print(repeated_substring_pattern("ababba"))
