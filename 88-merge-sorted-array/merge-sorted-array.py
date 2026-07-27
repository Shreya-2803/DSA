class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s1=m-1
        s2=n-1
        s=m+n-1
        while s1>=0 and s2>=0:
            if(nums1[s1]>nums2[s2]):
                nums1[s]=nums1[s1]
                s1-=1
            else:
                nums1[s]=nums2[s2]
                s2-=1
            s-=1
        while s2>=0:
            nums1[s]=nums2[s2]
            s2-=1
            s-=1
