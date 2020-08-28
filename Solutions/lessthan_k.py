class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        ans = []
        A.sort()
        
        start = 0
        end = len(A) - 1
        
        while start != end:
            
            if A[start] + A[end] >= K:
                end -= 1
            
            else:
                ans.append(A[start] + A[end])
                start += 1
        
        if ans:
            return max(ans)
        return -1
                
                    
                    
            
            
            