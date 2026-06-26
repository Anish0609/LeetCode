class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row=len(matrix)
        col=len(matrix[0])

        low=0
        high=row-1
        idx=-1

        while low<=high :
            guess=(low+high)//2

            if matrix[guess][0]<=target<=matrix[guess][col-1] :
                idx=guess
                break
            elif matrix[guess][col-1]<target :
                low=guess+1
            else :
                high=guess-1
            
        if idx==-1 :
            return False
        
        low=0
        high=col-1

        while low<=high :
            guess=(low+high)//2

            if matrix[idx][guess]==target :
                return True
            elif matrix[idx][guess]<target :
                low=guess+1
            else :
                high=guess-1
        return False
