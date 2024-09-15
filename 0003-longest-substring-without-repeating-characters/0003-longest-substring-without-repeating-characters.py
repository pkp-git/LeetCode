class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = ""
        count = 0
        maxlen = 0
        for i in range(0,len(s)):
            if s[i] not in chars:
                count += 1
                chars += s[i]
                print("s[i]/.",s[i], "./ if stat: ", count, "char:/.",chars,"./")
            else:
                print("begin else: s[i]/.",s[i],",/")
                chars = chars[::-1]
                print(chars)
                idx = chars.find(s[i])
                chars = s[i]+chars[:idx]
                print(chars[:idx])
                chars = chars[::-1]
                count = len(chars)
                print(idx, chars)
                print("char:/.",chars,"./")
            maxlen = max(count,maxlen)
            print(maxlen)
        return maxlen

        