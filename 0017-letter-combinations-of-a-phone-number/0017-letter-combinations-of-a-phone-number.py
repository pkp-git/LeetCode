class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []

        if not digits:
            return []
        
        def backtrack(i, curstring):
            if len(curstring) == len(digits):
                res.append(curstring)
                return 
            
            for char in phone[digits[i]]:
                backtrack(i+1, curstring + char)
            
        if digits: 
            backtrack(0, "")
        return res
            


