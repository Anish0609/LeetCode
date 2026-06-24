class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        n=len(arr)
        for i in range(n):
            if i>0 :
                if arr[i-1]>arr[i]:
                    x=i-1
                    return x
                    break
                
        



        

        