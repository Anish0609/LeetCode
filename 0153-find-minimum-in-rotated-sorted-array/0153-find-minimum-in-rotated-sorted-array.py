class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        n=len(nums)
        high=n-1

        while low<=high :
            guess=(low+high)//2

            if nums[guess]>nums[n-1] :
                low=guess+1
            else :
                res=nums[guess]
                high=guess-1
        
        return res
