class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        dist_map = {}
        dist_map_dup = {}
        dist = []
        ans = []
        
        for point in points:
            
            sq = point[0] ** 2 +  point[1] ** 2
            
            dist.append(sq)
            if sq in dist_map.keys():
                dist_map_dup[sq] = [point[0],point[1]]
            else:
                dist_map[sq] = [point[0],point[1]]
            
        
        dist.sort()
        
        for i in range(0,K):
            
            if dist[i] not in dist_map_dup.keys():
    
                ans.append(dist_map[dist[i]])
                
                
                
            else:
                if dist_map[dist[i]] and dist_map_dup[dist[i]] not in ans:
                    ans.append(dist_map[dist[i]])
                    ans.append(dist_map_dup[dist[i]])
                
        return ans
        