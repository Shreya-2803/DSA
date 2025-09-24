class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        res=[]
        if(numerator<0)^(denominator<0):
            res.append("-")
        numerator,denominator=abs(numerator),abs(denominator)
        res.append(str(numerator//denominator))
        rem=numerator%denominator
        if rem==0:
            return "".join(res)
        res.append(".")
        rem_map={}
        while rem:
            if rem in rem_map:
                idx=rem_map[rem]
                res.insert(idx,"(")
                res.append(")")
                break
            rem_map[rem]=len(res)
            rem*=10
            res.append(str(rem//denominator))
            rem%=denominator
        return "".join(res)
