class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []

        if not digits: 
            return []
        
        def back(i, tempchar):
            if len(tempchar) == len(digits):
                res.append(tempchar)
                return
            
            for c in phone[digits[i]]:
                back(i + 1, tempchar + c)
    
        if digits: 
            back(0,"")
        return res
            


