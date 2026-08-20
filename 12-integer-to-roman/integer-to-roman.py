class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        res=[]
        for symbol,value in hash_map.items():
            if num==0:
                break
            count=num//value
            if count>0:
                res.append(symbol*count)
                num%=value
        return "".join(res)