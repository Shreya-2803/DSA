class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p=nums[0]
        min_p=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            if num<0:
                max_p,min_p=min_p,max_p
            max_p=max(num,max_p*num)
            min_p=min(num,min_p*num)
            res=max(res,max_p)
        return res