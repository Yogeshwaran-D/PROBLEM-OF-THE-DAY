from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        adj=defaultdict(list)
        for v1 , v2 , dist in edges :
            adj[v1].append((v2,dist))
            adj[v2].append((v1,dist))

        def dijkstra(src):
            heap=[(0,src)]
            visited=set()
            while heap:
                dist,node=heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei , dist2 in adj[node]:
                    nei_dist= dist+dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap,(nei_dist,nei))
            return len(visited)-1

        res,min_count=-1,n
        for src in range(n):
            count=dijkstra(src)
            if count<=min_count:
                res,min_count=src,count
        return res