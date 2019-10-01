class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = 0
        lst = []
        
        for i in matrix:
            
            for j in i:
                
                lst.append(j)
                
        lst.sort()
        
        return lst[k-1]
                
                
                
                
                
                
        