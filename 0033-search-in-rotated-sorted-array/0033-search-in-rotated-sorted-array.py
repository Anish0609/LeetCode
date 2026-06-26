class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        n=len(nums)
        high=n-1
        res=-1

        while low<=high :
            guess=(low+high)//2

            if nums[guess]==target :
                return guess
            if nums[guess]>nums[n-1] :
                if nums[guess]<target :
                    low=guess+1
                elif nums[guess]>target :
                    if nums[0]<=target :
                        high=guess-1
                    else :
                        low=guess+1
            else :
                if nums[guess]>target :
                    high=guess-1
                elif nums[guess]<target :
                    if nums[n-1]>=target :
                        low=guess+1
                    else :
                        high=guess-1
        
        return res

        
        