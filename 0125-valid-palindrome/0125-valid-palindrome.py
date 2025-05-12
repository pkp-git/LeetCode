class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filteredlist = []

        for i in s:
            if i.isalnum():
                filteredlist.append(i.lower())

        s = ''.join(filteredlist)

        def checkpal(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return checkpal(l + 1, r - 1)

        return checkpal(0, len(s) - 1)

    