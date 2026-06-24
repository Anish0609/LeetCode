class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        n=len(nums)
        high=n-1
        first=last=-1
        res=[]

        while low<=high :
            guess=(low+high)//2

            if nums[guess]==target :
                first=guess
                high=guess-1
            elif nums[guess]<target :
                low=guess+1
            else :
                high=guess-1
        
        low=0
        high=n-1
        
        while low<=high :
            guess=(low+high)//2

            if nums[guess]==target :
                last=guess
                low=guess+1
            elif nums[guess]<target :
                low=guess+1
            else :
                high=guess-1

        res=[first,last]
        
        return res
        


        