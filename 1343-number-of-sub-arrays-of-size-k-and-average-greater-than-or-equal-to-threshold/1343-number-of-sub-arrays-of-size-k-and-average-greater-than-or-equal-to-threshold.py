class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        left=0
        count=0
        sum1=0
        avg=0
        for right in range(len(arr)):
            sum1+=arr[right]
            if right-left+1==k:
                if sum1>=k*threshold:
                    count+=1
                sum1-=arr[left]
                left+=1
        return count
        