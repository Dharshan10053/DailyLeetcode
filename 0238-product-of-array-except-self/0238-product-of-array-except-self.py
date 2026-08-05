class Solution(object):
    def productExceptSelf(self, nums):
        myarr=[1]*len(nums)
        prefix=1
        
        for i in range(len(nums)):
            myarr[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(len(nums)-1,-1,-1):
            myarr[i]*=suffix
            suffix*=nums[i]
        return myarr

            

        