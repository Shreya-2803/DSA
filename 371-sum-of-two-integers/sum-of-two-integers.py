class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while(b!=0):
            carry=(a&b)<<1
            a=(a^b)& mask
            b=carry & mask
        return a if a<=MAX else ~(a^mask)