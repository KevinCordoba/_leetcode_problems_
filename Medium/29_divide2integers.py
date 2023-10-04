class Solution(object):
    def divide(self, dividend, divisor):
        if(divisor == 0):
            return ("no divion by 0")
        else:
            cont = 0
            negativo = ((dividend < 0) ^ (divisor < 0))
            dividend = int(abs(dividend))
            divisor = int(abs(divisor))
            for i in range (1, dividend, divisor):
                cont += 1
        if (negativo):
                cont = -cont    
        return cont
    
c = Solution()
print(c.divide(7, -3))