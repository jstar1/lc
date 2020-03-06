#!/usr/bin/python


class Solution:
    def longest_common_prefix(self, words):
        if not words:
            return ""
        if len(words) == 1:
            return words[0]
        h1 = self.longest_common_prefix(words[len(words) // 2:])
        h2 = self.longest_common_prefix(words[:len(words) // 2])
        return self.merge(h1, h2)


    def merge(self, h1, h2):
        i = 0
        while i < len(h1) and i < len(h2) and h1[i] == h2[i]:
            print("h1: {}, h1[i]: {}".format(h1, h1[i]))
            print("h2: {}, h2[i]: {}".format(h2, h2[i]))
            print("i: {}".format(i))
            i += 1
        return h1[:i]
