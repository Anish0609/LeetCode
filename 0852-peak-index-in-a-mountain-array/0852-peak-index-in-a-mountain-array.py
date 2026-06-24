class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        n=len(arr)
        low=0
        high=n-1

        while low<=high :
            guess=(low+high)//2

            if arr[guess]<arr[guess+1] :
                low=guess+1
            elif arr[guess]>arr[guess+1] :
                res=guess
                high=guess-1
            
        return res
        

        



        

        