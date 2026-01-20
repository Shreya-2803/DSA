class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(check_str):
            return check_str==check_str[::-1]

        def backtrack(start,end,temp):
            if start==end:
                res.append(temp)
            for i in range(start,end):
                if is_palindrome(s[start:i+1]):
                    backtrack(i+1,end,temp+[s[start:i+1]])
        res=[]
        backtrack(0,len(s),[])
        return res
    