class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        stack = []
        
        for i in nums:
            
            if i not in stack:
                
                stack.append(i)
            
            else:
                
                stack.pop()
                
        
        return stack.pop()