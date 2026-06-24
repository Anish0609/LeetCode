class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        n=len(nums)
        high=n-1
        guess=0

        while low<=high :
            guess=(low+high)//2

            if nums[guess]==target :
                return guess
            elif nums[guess]<target :
                low=guess+1
            else :
                high=guess-1
            
        return -1

        