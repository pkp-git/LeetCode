class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.strip().split(" ")
        re = []
        
        print(lis)
        for i in range(len(lis)-1, -1, -1):
            if lis[i] != "":
                re.append(lis[i])
                print(lis[i])
        
        lis = ""
        lis = " ".join(re)
        return lis