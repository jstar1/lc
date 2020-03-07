#!/usr/bin/python3


class Solution:
    def valid_parens(self, parens):
        stack = []
        dic = { "]": "[", "}": "{", ")": "(" }
        for char in parens:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

