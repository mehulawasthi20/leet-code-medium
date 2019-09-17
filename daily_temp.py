class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ans = [0] * len(T)
        
        stack = []
        
        for i,t in enumerate(T):
            
            while stack and  t > T[stack[-1]] :
                
                curr = stack.pop()
                print(curr)
                ans[curr] = abs(i-curr)
               
                
            stack.append(i)
        
        return ans
        