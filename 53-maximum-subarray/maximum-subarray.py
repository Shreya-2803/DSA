class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        maxending=nums[0]
        for i in range(1,len(nums)):
            maxending=max(maxending+nums[i],nums[i])
            res=max(maxending,res)
        return res
        # sorted_array=sorted(nums)
        # maxvalue=nums[0]
        # total=0
        # for i in range(len(nums)):
        #     total+=nums[i]
        #     if total>maxvalue:
        #         maxvalue=total
        #     if total<0:
        #         total=0
        # return maxvalue
