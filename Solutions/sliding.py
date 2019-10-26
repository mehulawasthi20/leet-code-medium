class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        l = k-1
        if len(nums) == 0:
            return
        
        for i in range(0,len(nums)-l):
            ans.append(max(nums[0+i:i+k]))
        
        return ans