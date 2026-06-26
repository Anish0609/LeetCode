class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        # Find the row
        low, high = 0, rows - 1
        idx = -1

        while low <= high:
            guess = (low + high) // 2

            if matrix[guess][0] <= target <= matrix[guess][cols - 1]:
                idx = guess
                break
            elif target < matrix[guess][0]:
                high = guess - 1
            else:
                low = guess + 1

        if idx == -1:
            return False

        # Search inside the row
        low, high = 0, cols - 1

        while low <= high:
            guess = (low + high) // 2

            if matrix[idx][guess] == target:
                return True
            elif matrix[idx][guess] < target:
                low = guess + 1
            else:
                high = guess - 1

        return False