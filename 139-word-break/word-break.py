from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        @cache
        def solve(i):
            if i==len(s):
                return True
            for j in range(i+1,len(s)+1):
                word=s[i:j]
                if word in wordset and solve(j):
                    return True
            return False
        return solve(0)