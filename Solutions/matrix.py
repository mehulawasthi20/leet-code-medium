class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        for i in range(0,len(matrix)):
            
            if target > matrix[i][-1]:
                continue
            
            for j in range(0,len(matrix[0])):
                
                if target > matrix[-1][j]:
                    continue
                
                if target == matrix[i][j]:
                    return True
            
        
        return False