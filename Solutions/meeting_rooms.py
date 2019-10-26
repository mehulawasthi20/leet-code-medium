class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        if len(intervals) == 0:
            return 0
        
        rooms = []
        intervals.sort()
        heapq.heappush(rooms,intervals[0][1])
        
        for i in range(1,len(intervals)):
            
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms,intervals[i][1])
            
        
        return len(rooms)
        