class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row=len(matrix)
        col=len(matrix[0])

        low=0
        high=(row*col)-1

        while low<=high :
            guess=(low+high)//2

            x=guess//col
            y=guess%col

            if matrix[x][y]==target :
                return True
            elif matrix[x][y]<target :
                low=guess+1
            else :
                high=guess-1
        
        return False
            
