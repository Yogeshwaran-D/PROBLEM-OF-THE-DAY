from collections import deque
class Solution:
    def findTheWinner(self, n, k) :
        queue=deque()
        for i in range(1,n+1):
            queue.append(i)
        while len(queue) > 1:
            for _ in range(k-1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]