class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        ans = []
        
        ans = nums1+nums2
        ans.sort()
        
        if len(ans) % 2 == 0:
            mid_1 = len(ans)/2
            mid_2 = mid_1 + 1
        
        else:
            mid = len(ans)/2 + 0.5
        
        if len(ans) % 2 == 0:
            
            return (ans[int(mid_1-1)]+ans[int(mid_2-1)])/2
        else:
            return ans[int(mid-1)]
        
            
        