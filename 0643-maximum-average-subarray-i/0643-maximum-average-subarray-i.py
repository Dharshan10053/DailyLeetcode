class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        sum1=0
        avg=0
        max_avg=float('-inf')
        for right in range(len(nums)):
            sum1+=float(nums[right])
            if right-left+1==k:
                avg=sum1/k
                max_avg=max(avg,max_avg)
                sum1-=nums[left]
                left+=1
        return max_avg

        