class Solution(object):
    def maxAbsoluteSum(self, nums):
        current_sum1=0
        current_sum2=0
        max_sum=float("-inf")
        min_sum=float("+inf")
        for i in range(len(nums)):
            current_sum1=max(nums[i],nums[i]+current_sum1)
            max_sum=max(current_sum1,max_sum)
            current_sum2=min(nums[i],nums[i]+current_sum2)
            min_sum=min(current_sum2,min_sum)
        if max_sum>abs(min_sum):
            return max_sum
        else:
            return abs(min_sum)