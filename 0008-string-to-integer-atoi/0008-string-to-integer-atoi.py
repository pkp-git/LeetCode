class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        startflag = False
        sign = 1
        i = 0
        result = 0
        ignore = ["+", "-"]
        atoi = ""

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i+=1
        result = result * sign

        mini = -2**31
        maxi = 2**31 - 1

        if result < mini:
            return mini
        elif result > maxi:
            return maxi
        else:
            return result 