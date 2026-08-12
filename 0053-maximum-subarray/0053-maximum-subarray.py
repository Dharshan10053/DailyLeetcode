class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        sum1=0
        max_sum=float("-inf")
        for right in range(len(nums)):
            sum1=max(nums[right],sum1+nums[right])
            max_sum=max(sum1,max_sum)
        return max_sum
        