class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                sum+=nums[i]
        return sum
