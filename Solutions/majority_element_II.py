class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = []
        l = len(nums)
        
        limit = l/3
        
        limit = int(limit)
        
        for i in nums:
            
            if i in ans:
                continue
            if nums.count(i) > limit:
                ans.append(i)
                    
        
        return ans
    
        