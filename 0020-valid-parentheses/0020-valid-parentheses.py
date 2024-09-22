class Solution:
    def isValid(self, s: str) -> bool:  
        l = []
        d = {'(':')','{':'}','[':']'}
        for i in s:
            if i in "({[":
                l.append(i)
            elif l and i == d[l[-1]]:
                l.pop()
            else:
                return False
        return len(l) == 0

                
