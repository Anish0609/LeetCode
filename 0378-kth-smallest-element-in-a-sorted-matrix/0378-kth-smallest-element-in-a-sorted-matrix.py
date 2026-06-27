class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def small(num) :
            row=(len(matrix))-1
            col=0
            count=0

            while row>=0 and col<=(len(matrix[0]))-1 :
                if matrix[row][col]<=num :
                    count+=row+1
                    col+=1
                else :
                    row-=1
            return count
        
        row=len(matrix)
        col=len(matrix[0])
        
        low=matrix[0][0]
        high=matrix[row-1][col-1]
        ans=0
        res=-1

        while low<=high :
            guess=(low+high)//2

            ans=small(guess)

            if ans>=k :
                res=guess
                high=guess-1
            else :
                low=guess+1
        
        return res 

        