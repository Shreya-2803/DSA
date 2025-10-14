class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if 2*k>len(nums):
            return False
        def increasing(sub_arr):
            for i in range(len(sub_arr)-1):
                if sub_arr[i]>=sub_arr[i+1]:
                    return False
            return True
        n=len(nums)
        for i in range(n-2*k+1):
            sub_arr1=nums[i:i+k]
            sub_arr2=nums[i+k:i+2*k]

            if increasing(sub_arr1) and increasing(sub_arr2):
                return True
        return False
