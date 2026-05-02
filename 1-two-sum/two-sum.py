class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            d=target-nums[i]
            if d in seen:
                return [seen[d],i]
            else:
                seen[nums[i]]=i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        