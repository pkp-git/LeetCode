class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hindex = 0
        fi = 0
        citations.sort(reverse = True)
        for i in range(0,len(citations)):
            fi = citations[i]
            if (fi >= i+1):
                hindex+=1
        return hindex
