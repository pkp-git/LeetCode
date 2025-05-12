class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1: 
            return 1
        
        count = 1 

        def fibo(l,r,count):
            if count == n: 
                return r
            res = l + r
            count += 1
            return fibo(r,res,count)
        
        return fibo(0,1,count)