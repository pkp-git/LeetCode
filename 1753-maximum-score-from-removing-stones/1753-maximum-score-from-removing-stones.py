def sorti(arr,size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
class Solution:    
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = [a,b,c]
        sorti(l,len(l))
        count = 0

        while len(l)>1:
            r1 = l.pop()
            r2 = l.pop()

            r1 -=1
            r2 -=1
            count += 1

            if r1>0:
                l.append(r1)
            if r2>0:
                l.append(r2)
            
            sorti(l,len(l))
        return count