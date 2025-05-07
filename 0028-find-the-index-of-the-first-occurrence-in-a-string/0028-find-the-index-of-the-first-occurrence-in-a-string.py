class Solution:
    def strStr(self, haystack, needle):
        needlen = len(needle)
        for i in range(len(haystack)-needlen+1):
            if haystack[i:i+needlen] == needle:
                return i
        return -1