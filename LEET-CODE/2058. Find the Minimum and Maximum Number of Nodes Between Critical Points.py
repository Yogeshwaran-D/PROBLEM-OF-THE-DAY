class Solution:
    def nodesBetweenCriticalPoints(self, head):
        current=head
        pre=None
        index=1
        res=[]
        while current.next:
            if pre is not None:
                if pre > current.val < current.next.val or pre < current.val > current.next.val:
                    res.append(index)
            pre=current.val
            current=current.next
            index+=1
        if len(res) < 2 :
            return[-1,-1]
        minDistance=100000000
        for i in range(len(res)-1):
            minDistance=min(minDistance,res[i+1]-res[i])
        return [minDistance,res[-1]-res[0]]