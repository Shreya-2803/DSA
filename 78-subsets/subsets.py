class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(st,end):
            res.append(end)
            for i in range(st,len(nums)):
                backtrack(i+1,end+[nums[i]])
        res=[]
        backtrack(0,[])
        return res