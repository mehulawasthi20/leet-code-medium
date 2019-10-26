class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        
        for i in strs:
            x = tuple(sorted(i))
            #print(x)
            if x not in dic.keys():
                
                dic[x] = [i]
            
            else:
                dic[x].append(i)
        
        return dic.values()
        
    