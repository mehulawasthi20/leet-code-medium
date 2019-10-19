class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digits = []
        letters = []
        
        
        for log in logs:
            
            #for j in log:
                
            if log.split()[1].isdigit():
                    
                digits.append(log)
                
            else:
                letters.append(log)
            
        
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])
        
        letters = letters + digits
        
        return letters
        
        
        
                    
                
                
        
        
        