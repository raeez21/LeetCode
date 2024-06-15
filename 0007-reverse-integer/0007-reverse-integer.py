class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        
        while x:
            digit = x % 10
            r = r*10 + digit
            x //= 10
        
        r= sign * r
        if (r > 2 ** 31 - 1) or (r < -(2 ** 31)):
            return 0
        return r
    
            
        