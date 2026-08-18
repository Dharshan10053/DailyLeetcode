class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr=[]
        for nums in nums1:
            if nums in nums2:
                arr.append(nums)
                
        return list(set(arr))
            