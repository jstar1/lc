#!/usr/bin/python3


class Solution:
    def roman_int(self, s):
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        for i in range(0, len(s) - 1):
            if symbols[s[i]] < symbols[s[i+1]]:
                count -= symbols[s[i]]
            else:
                count += symbols[s[i]]
        return count + symbols[s[-1]]
