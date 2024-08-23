import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1

        digits = re.split('/|(?=[-+])', expression)
        digits = list(filter(None, digits))
        
        for i in range(0, len(digits), 2):
            currNum = int(digits[i])
            currDenom = int(digits[i + 1])
            
            num = num * currDenom + currNum * denom
            denom = denom * currDenom
            
        gcd = abs(self.findGCD(num, denom))
        
        num //= gcd
        denom //= gcd

        return str(num) + "/" + str(denom)

    def findGCD(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        return self.findGCD(b, a % b)