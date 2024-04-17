class Solution:
    def roman_to_int(self, s: str) -> int:
        symbol_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        for x in range(len(s)):
            value = self.normalized_value(s, symbol_to_value[s[x]], x)
            result += value

        return result

    def normalized_value(self, s: str, cur_val: int, cur_pos: int) -> int:
        if cur_pos + 1 >= len(s):
            return cur_val

        cur_text = s[cur_pos]
        next_text = s[cur_pos + 1]

        if cur_text == 'I' and (next_text == 'V' or next_text == 'X'):
            cur_val = -1
        elif cur_text == 'X' and (next_text == 'L' or next_text == 'C'):
            cur_val = -10
        elif cur_text == 'C' and (next_text == 'D' or next_text == 'M'):
            cur_val = -100

        return cur_val


solution = Solution()
val = solution.roman_to_int("MCMXCIV")
print(val)
